"""
Test script to verify the system is set up correctly
"""
import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def test_imports():
    """Test if all required packages can be imported"""
    print("Testing imports...")
    try:
        import streamlit
        import langchain
        import chromadb
        import openai
        import bs4
        import requests
        print("✅ All imports successful")
        return True
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False

def test_env():
    """Test if environment variables are set"""
    print("\nTesting environment variables...")
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key and api_key != "your_openai_api_key_here":
        print("✅ OPENAI_API_KEY is set")
        return True
    else:
        print("❌ OPENAI_API_KEY not set or using placeholder")
        return False

def test_directories():
    """Test if required directories exist"""
    print("\nTesting directories...")
    dirs = ['data', 'data/scraped', 'vector_store']
    all_exist = True
    for dir_path in dirs:
        path = Path(dir_path)
        if path.exists():
            print(f"✅ {dir_path} exists")
        else:
            print(f"⚠️  {dir_path} does not exist (will be created automatically)")
            all_exist = False
    return True

def test_data_collection():
    """Test if scraped data exists"""
    print("\nTesting data collection...")
    data_file = Path("data/scraped/all_sources.json")
    if data_file.exists():
        import json
        with open(data_file, 'r') as f:
            data = json.load(f)
        print(f"✅ Scraped data exists ({len(data)} sources)")
        return True
    else:
        print("⚠️  No scraped data found. Run: python data_collector.py")
        return False

def test_vector_store():
    """Test if vector store exists"""
    print("\nTesting vector store...")
    try:
        from vector_store import VectorStore
        vs = VectorStore()
        try:
            vs.load_vector_store()
            print("✅ Vector store exists")
            return True
        except:
            print("⚠️  Vector store not found. Run: python vector_store.py")
            return False
    except Exception as e:
        print(f"❌ Error testing vector store: {e}")
        return False

def test_rag_pipeline():
    """Test if RAG pipeline can be initialized"""
    print("\nTesting RAG pipeline...")
    try:
        from rag_pipeline import RAGPipeline
        pipeline = RAGPipeline()
        print("✅ RAG pipeline initialized successfully")
        return True
    except Exception as e:
        print(f"⚠️  RAG pipeline initialization issue: {e}")
        print("   This might be expected if data/vector store is not set up yet")
        return False

def main():
    print("=" * 60)
    print("Mutual Fund Facts Assistant - System Test")
    print("=" * 60)
    print()
    
    results = []
    
    results.append(("Imports", test_imports()))
    results.append(("Environment", test_env()))
    results.append(("Directories", test_directories()))
    results.append(("Data Collection", test_data_collection()))
    results.append(("Vector Store", test_vector_store()))
    results.append(("RAG Pipeline", test_rag_pipeline()))
    
    print("\n" + "=" * 60)
    print("Test Summary")
    print("=" * 60)
    
    for name, result in results:
        status = "✅ PASS" if result else "⚠️  CHECK"
        print(f"{name:20} {status}")
    
    critical = [name for name, result in results[:2] if not result]
    if critical:
        print(f"\n❌ Critical issues found: {', '.join(critical)}")
        print("Please fix these before running the application.")
        return False
    else:
        print("\n✅ System is ready!")
        print("You can now run: streamlit run app.py")
        return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)

