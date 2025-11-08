"""
Vector store setup and management for RAG system
"""
import chromadb
from chromadb.config import Settings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.schema import Document
import json
import logging
from pathlib import Path
from typing import List, Dict
import config

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class VectorStore:
    """Manages vector store for RAG system"""
    
    def __init__(self):
        self.embeddings = OpenAIEmbeddings(model=config.EMBEDDING_MODEL)
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=config.CHUNK_SIZE,
            chunk_overlap=config.CHUNK_OVERLAP,
            length_function=len,
        )
        self.vector_store_path = config.VECTOR_STORE_DIR
        
        # Initialize ChromaDB
        self.client = chromadb.PersistentClient(
            path=str(self.vector_store_path),
            settings=Settings(anonymized_telemetry=False)
        )
        
        self.vector_store = None
        
    def create_documents_from_data(self, data: List[Dict]) -> List[Document]:
        """Convert scraped data to LangChain documents"""
        documents = []
        
        for item in data:
            # Create document with metadata
            doc_content = f"Title: {item.get('title', '')}\n\n{item.get('content', '')}"
            
            # Split into chunks
            chunks = self.text_splitter.split_text(doc_content)
            
            for i, chunk in enumerate(chunks):
                doc = Document(
                    page_content=chunk,
                    metadata={
                        'source': item.get('url', ''),
                        'title': item.get('title', ''),
                        'chunk_index': i,
                        'total_chunks': len(chunks)
                    }
                )
                documents.append(doc)
        
        logger.info(f"Created {len(documents)} documents from {len(data)} sources")
        return documents
    
    def build_vector_store(self, documents: List[Document], recreate: bool = False):
        """Build or update vector store"""
        if recreate:
            # Delete existing collection
            try:
                self.client.delete_collection(name=config.COLLECTION_NAME)
            except:
                pass
        
        # Create vector store
        self.vector_store = Chroma.from_documents(
            documents=documents,
            embedding=self.embeddings,
            collection_name=config.COLLECTION_NAME,
            persist_directory=str(self.vector_store_path),
            client=self.client
        )
        
        logger.info(f"Vector store built with {len(documents)} documents")
    
    def load_vector_store(self):
        """Load existing vector store"""
        try:
            self.vector_store = Chroma(
                collection_name=config.COLLECTION_NAME,
                embedding_function=self.embeddings,
                persist_directory=str(self.vector_store_path),
                client=self.client
            )
            # Quick check to ensure collection is not empty
            _ = self.vector_store.get()
            logger.info("Vector store loaded")
        except Exception as e:
            logger.warning(f"Vector store load failed: {e}")
            self.vector_store = None
            raise
    
    def search(self, query: str, k: int = config.TOP_K_RESULTS) -> List[Document]:
        """Search vector store for relevant documents"""
        if not self.vector_store:
            self.load_vector_store()
        
        results = self.vector_store.similarity_search_with_score(
            query, k=k
        )
        
        # Return documents (without scores for now)
        return [doc for doc, score in results]
    
    def search_with_sources(self, query: str, k: int = config.TOP_K_RESULTS) -> List[Dict]:
        """Search and return results with source URLs"""
        documents = self.search(query, k)
        
        results = []
        seen_sources = set()
        
        for doc in documents:
            source_url = doc.metadata.get('source', '')
            if source_url and source_url not in seen_sources:
                results.append({
                    'content': doc.page_content,
                    'source': source_url,
                    'title': doc.metadata.get('title', '')
                })
                seen_sources.add(source_url)
        
        return results

if __name__ == "__main__":
    from data_collector import DataCollector
    
    # Collect data
    collector = DataCollector()
    data = collector.load_scraped_data()
    
    if not data:
        logger.info("No scraped data found. Collecting now...")
        data = collector.collect_all_sources()
    
    # Build vector store
    vs = VectorStore()
    documents = vs.create_documents_from_data(data)
    vs.build_vector_store(documents, recreate=True)

