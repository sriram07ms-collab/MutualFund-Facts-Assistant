"""
RAG pipeline for generating factual responses with citations
"""
import os
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema import HumanMessage, SystemMessage
from typing import List, Dict, Optional
import logging
import config
from vector_store import VectorStore
from datetime import datetime
from data_collector import DataCollector

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class RAGPipeline:
    """RAG pipeline for answering factual questions"""
    
    def __init__(self):
        self.llm = ChatOpenAI(
            model=config.LLM_MODEL,
            temperature=config.TEMPERATURE,
            max_tokens=config.MAX_TOKENS
        )
        self.vector_store = VectorStore()
        self._ensure_vector_store()

    def _ensure_vector_store(self):
        """Ensure the vector store is available; build if missing."""
        try:
            self.vector_store.load_vector_store()
        except Exception:
            logger.info("Vector store not found. Collecting data and rebuilding.")
            collector = DataCollector()
            data = collector.load_scraped_data()
            if not data:
                data = collector.collect_all_sources()
            documents = self.vector_store.create_documents_from_data(data)
            self.vector_store.build_vector_store(documents, recreate=True)
            self.vector_store.load_vector_store()
        
    def is_advice_request(self, query: str) -> bool:
        """Check if query is asking for investment advice"""
        query_lower = query.lower()
        return any(keyword in query_lower for keyword in config.ADVICE_KEYWORDS)
    
    def generate_response(self, query: str) -> Dict:
        """Generate response with citation"""
        
        # Check for advice requests
        if self.is_advice_request(query):
            return {
                'answer': config.ADVICE_REFUSAL_MESSAGE,
                'source': 'https://www.amfiindia.com/investor-corner/knowledge-center/faqs',
                'is_advice': True
            }
        
        # Search vector store
        search_results = self.vector_store.search_with_sources(query)
        
        if not search_results:
            return {
                'answer': "I couldn't find specific information about your query in the official sources. Please try rephrasing your question or check the official AMC website.",
                'source': config.SOURCE_URLS.get('nippon_main', 'https://mf.nipponindiaim.com/'),
                'is_advice': False
            }
        
        # Prepare context from search results
        context_parts = []
        sources = []
        
        for result in search_results[:3]:  # Use top 3 results
            context_parts.append(f"Source: {result['title']}\nContent: {result['content'][:500]}")
            sources.append(result['source'])
        
        context = "\n\n".join(context_parts)
        primary_source = sources[0] if sources else config.SOURCE_URLS.get('nippon_main', 'https://mf.nipponindiaim.com/')
        
        # Create prompt
        system_prompt = """You are a Facts-Only Mutual Fund AI Assistant. Your role is to answer factual questions about mutual fund schemes using ONLY the information provided in the context.

Rules:
1. Answer ONLY factual questions (expense ratio, exit load, minimum SIP, lock-in period, riskometer, benchmark, statement downloads, NAV, fund details)
2. Keep answers concise (maximum 3 sentences, preferably 1-2)
3. Base your answer ONLY on the provided context
4. If the context doesn't contain the answer, respond: "I couldn't find specific information about [topic] in the official sources. Please check the official AMC website or contact the fund house directly."
5. Never provide investment advice, recommendations, or opinions
6. Never compare funds or make performance predictions
7. Extract exact numbers, percentages, and dates from the context when available
8. Do not include "Source:" in your response - it will be added automatically

Format your response as:
[Concise factual answer in 1-3 sentences with specific numbers/percentages if available]"""

        human_prompt = f"""Context from official sources:
{context}

Question: {query}

Provide a factual answer based on the context above. If the answer is not in the context, say so."""

        try:
            # Generate response
            messages = [
                SystemMessage(content=system_prompt),
                HumanMessage(content=human_prompt)
            ]
            
            response = self.llm.invoke(messages)
            answer = response.content.strip()
            
            # Remove any existing "Source:" mentions from LLM response
            answer = answer.split("Source:")[0].strip()
            
            # Add source and timestamp
            answer += f"\n\nSource: {primary_source}"
            last_updated = datetime.now().strftime("%Y-%m-%d")
            answer += f"\n\nLast updated from sources: {last_updated}"
            
            return {
                'answer': answer,
                'source': primary_source,
                'is_advice': False
            }
            
        except Exception as e:
            logger.error(f"Error generating response: {e}")
            return {
                'answer': "I encountered an error while processing your query. Please try again or check the official sources directly.",
                'source': primary_source,
                'is_advice': False
            }

if __name__ == "__main__":
    # Test the pipeline
    pipeline = RAGPipeline()
    
    test_queries = [
        "What is the expense ratio of Nippon India Large Cap Fund?",
        "What is the minimum SIP amount?",
        "Should I buy this fund?"
    ]
    
    for query in test_queries:
        print(f"\nQuery: {query}")
        result = pipeline.generate_response(query)
        print(f"Answer: {result['answer']}")
        print(f"Source: {result['source']}")

