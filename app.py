"""
Streamlit app for Mutual Fund Facts Assistant
Inspired by Groww's clean, modern UI design
"""
import streamlit as st
import os
from dotenv import load_dotenv
import config
from rag_pipeline import RAGPipeline
from data_collector import DataCollector
from vector_store import VectorStore

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title=config.APP_TITLE,
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for Groww-inspired design
st.markdown("""
<style>
    /* Main container */
    .main {
        padding-top: 2rem;
    }
    
    /* Header styling */
    .header-container {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(135deg, #00D09C 0%, #00B887 100%);
        border-radius: 12px;
        margin-bottom: 2rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    .header-title {
        color: white;
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    
    .header-subtitle {
        color: rgba(255, 255, 255, 0.9);
        font-size: 1.1rem;
        margin-bottom: 1rem;
    }
    
    .disclaimer {
        background-color: #FFF4E6;
        border-left: 4px solid #FFA726;
        padding: 1rem;
        border-radius: 4px;
        margin: 1rem 0;
        font-size: 0.9rem;
        color: #E65100;
    }
    
    /* Chat message styling */
    .user-message {
        background-color: #E3F2FD;
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
        border-left: 4px solid #2196F3;
    }
    
    .assistant-message {
        background-color: #F5F5F5;
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
        border-left: 4px solid #00D09C;
    }
    
    .source-link {
        color: #00B887;
        text-decoration: none;
        font-weight: 500;
        font-size: 0.9rem;
        margin-top: 0.5rem;
        display: inline-block;
    }
    
    .source-link:hover {
        text-decoration: underline;
    }
    
    /* Example questions */
    .example-question {
        background-color: white;
        border: 1px solid #E0E0E0;
        border-radius: 8px;
        padding: 0.75rem 1rem;
        margin: 0.5rem 0;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    
    .example-question:hover {
        border-color: #00D09C;
        background-color: #F0FDFA;
        transform: translateX(5px);
    }
    
    /* Input styling */
    .stTextInput > div > div > input {
        border-radius: 8px;
        border: 2px solid #E0E0E0;
        padding: 0.75rem;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #00D09C;
    }
    
    /* Button styling */
    .stButton > button {
        background-color: #00D09C;
        color: white;
        border-radius: 8px;
        border: none;
        padding: 0.75rem 2rem;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        background-color: #00B887;
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0, 208, 156, 0.3);
    }
    
    /* Hide Streamlit default elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'pipeline' not in st.session_state:
    st.session_state.pipeline = None
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'initialized' not in st.session_state:
    st.session_state.initialized = False

def initialize_system():
    """Initialize RAG pipeline and vector store"""
    if not st.session_state.initialized:
        # Check for API key
        if not os.getenv("OPENAI_API_KEY"):
            return False, "OpenAI API key not found. Please set OPENAI_API_KEY in your environment variables or Streamlit secrets."
        
        with st.spinner("Initializing system..."):
            try:
                # Check if vector store exists
                vector_store = VectorStore()
                
                # Try to load vector store
                try:
                    vector_store.load_vector_store()
                    
                    # Check if collection has documents
                    try:
                        collection = vector_store.client.get_collection(config.COLLECTION_NAME)
                        if collection.count() == 0:
                            # Try to collect data automatically
                            st.info("Vector store is empty. Collecting data from official sources...")
                            collector = DataCollector()
                            data = collector.collect_all_sources()
                            if data:
                                documents = vector_store.create_documents_from_data(data)
                                vector_store.build_vector_store(documents, recreate=True)
                                st.success("Data collected successfully!")
                            else:
                                return False, "Failed to collect data. Please try again using the sidebar button."
                    except Exception as e:
                        # Collection doesn't exist, try to build it
                        st.info("Building vector store from data...")
                        collector = DataCollector()
                        data = collector.load_scraped_data()
                        if not data:
                            data = collector.collect_all_sources()
                        if data:
                            documents = vector_store.create_documents_from_data(data)
                            vector_store.build_vector_store(documents, recreate=True)
                            st.success("Vector store built successfully!")
                        else:
                            return False, f"Vector store collection not found and data collection failed. Error: {str(e)}"
                except Exception as e:
                    # Vector store doesn't exist, try to create it
                    st.info("Creating vector store...")
                    collector = DataCollector()
                    data = collector.load_scraped_data()
                    if not data:
                        data = collector.collect_all_sources()
                    if data:
                        documents = vector_store.create_documents_from_data(data)
                        vector_store.build_vector_store(documents, recreate=False)
                        st.success("Vector store created successfully!")
                    else:
                        return False, f"Vector store not found and data collection failed. Error: {str(e)}"
                
                # Initialize pipeline
                st.session_state.pipeline = RAGPipeline()
                st.session_state.initialized = True
                return True, "System initialized successfully"
            except Exception as e:
                return False, f"Error initializing system: {str(e)}"
    return True, "System already initialized"

def main():
    # Header
    st.markdown("""
    <div class="header-container">
        <div class="header-title">📊 Mutual Fund Facts Assistant</div>
        <div class="header-subtitle">Get factual answers about mutual fund schemes from official sources</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Disclaimer
    st.markdown("""
    <div class="disclaimer">
        <strong>⚠️ Facts-only. No investment advice.</strong> This assistant provides factual information from official AMC, SEBI, and AMFI sources. Always consult a registered investment advisor for investment decisions.
    </div>
    """, unsafe_allow_html=True)
    
    # Initialize system
    initialized, message = initialize_system()
    if not initialized:
        st.error(f"❌ {message}")
        st.info("""
        💡 **Setup Instructions:**
        
        1. **Set your OpenAI API key** in `.env` file:
           ```
           OPENAI_API_KEY=your_key_here
           ```
        
        2. **Collect data** from official sources using the sidebar button or run:
           ```bash
           python data_collector.py
           ```
        
        3. **Build vector store** (automatically done after data collection) or run:
           ```bash
           python vector_store.py
           ```
        
        4. **Refresh this page** to start using the assistant
        """)
        return
    
    # Sidebar for data management
    with st.sidebar:
        st.header("⚙️ System Management")
        st.markdown("---")
        
        if st.button("🔄 Refresh Data & Rebuild", use_container_width=True):
            try:
                with st.spinner("Collecting data from official sources..."):
                    collector = DataCollector()
                    data = collector.collect_all_sources()
                    
                    if data:
                        st.success(f"✅ Collected {len(data)} sources")
                        
                        # Rebuild vector store
                        with st.spinner("Building vector store..."):
                            vs = VectorStore()
                            documents = vs.create_documents_from_data(data)
                            vs.build_vector_store(documents, recreate=True)
                            st.success("✅ Vector store built successfully")
                            
                            # Reset initialization
                            st.session_state.initialized = False
                            st.session_state.pipeline = None
                            st.rerun()
                    else:
                        st.error("❌ Failed to collect data. Please check your internet connection.")
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
        
        st.markdown("---")
        st.markdown("### 📊 System Status")
        if st.session_state.initialized:
            st.success("✅ System Ready")
        else:
            st.warning("⚠️ System Not Initialized")
        
        st.markdown("---")
        st.markdown("### 📚 Resources")
        st.markdown("""
        - [Nippon India MF](https://mf.nipponindiaim.com/)
        - [AMFI](https://www.amfiindia.com/)
        - [SEBI](https://www.sebi.gov.in/)
        """)
    
    # Main chat interface
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.subheader("💬 Ask a Question")
    
    # Example questions
    st.markdown("### 📝 Example Questions")
    example_cols = st.columns(3)
    
    for i, question in enumerate(config.EXAMPLE_QUESTIONS):
        with example_cols[i % 3]:
            if st.button(f"❓ {question}", key=f"example_{i}", use_container_width=True):
                # Add to chat
                st.session_state.messages.append({
                    "role": "user",
                    "content": question
                })
                st.rerun()
    
    # Display chat history
    if st.session_state.messages:
        st.markdown("### 💭 Conversation")
        for message in st.session_state.messages:
            if message["role"] == "user":
                st.markdown(f"""
                <div class="user-message">
                    <strong>You:</strong> {message["content"]}
                </div>
                """, unsafe_allow_html=True)
            else:
                answer_text = message["content"]["answer"]
                # Convert markdown-style formatting to HTML
                answer_text = answer_text.replace('\n\n', '<br><br>').replace('\n', '<br>')
                source_url = message["content"]["source"]
                
                st.markdown(f"""
                <div class="assistant-message">
                    <strong>Assistant:</strong><br><br>
                    {answer_text}
                    <br><br>
                    <a href="{source_url}" target="_blank" class="source-link">
                        📎 View Source
                    </a>
                </div>
                """, unsafe_allow_html=True)
    
    # Chat input
    st.markdown("---")
    user_input = st.text_input(
        "Ask your question:",
        placeholder="e.g., What is the expense ratio of Nippon India Large Cap Fund?",
        key="user_input"
    )
    
    col1, col2 = st.columns([1, 5])
    with col1:
        send_button = st.button("Send", use_container_width=True)
    
    # Process query
    if send_button and user_input:
        # Add user message
        st.session_state.messages.append({
            "role": "user",
            "content": user_input
        })
        
        # Generate response
        with st.spinner("Searching official sources..."):
            try:
                response = st.session_state.pipeline.generate_response(user_input)
                
                # Add assistant response
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": response
                })
                
                st.rerun()
            except Exception as e:
                st.error(f"Error: {str(e)}")
                st.info("Please check that your OpenAI API key is set correctly in the `.env` file.")

if __name__ == "__main__":
    main()

