"""
Setup script for Mutual Fund Facts Assistant
"""
import os
import sys
from pathlib import Path

def check_dependencies():
    """Check if required packages are installed"""
    required_packages = [
        'streamlit',
        'langchain',
        'langchain-community',
        'langchain-openai',
        'chromadb',
        'beautifulsoup4',
        'requests',
        'python-dotenv',
        'openai'
    ]
    
    missing_packages = []
    for package in required_packages:
        try:
            __import__(package.replace('-', '_'))
        except ImportError:
            missing_packages.append(package)
    
    return missing_packages

def check_env_file():
    """Check if .env file exists and has OpenAI API key"""
    env_file = Path('.env')
    if not env_file.exists():
        return False, "❌ .env file not found. Please create one with your OPENAI_API_KEY."
    
    with open(env_file, 'r') as f:
        content = f.read()
        if 'OPENAI_API_KEY' not in content or 'your_openai_api_key_here' in content:
            return False, "⚠️ OPENAI_API_KEY not set in .env file. Please add your API key."
    
    return True, "✅ .env file is configured correctly"

def setup_directories():
    """Create necessary directories"""
    directories = [
        'data',
        'data/scraped',
        'vector_store'
    ]
    
    for dir_path in directories:
        Path(dir_path).mkdir(parents=True, exist_ok=True)
    
    return True

def main():
    print("=" * 60)
    print("Mutual Fund Facts Assistant - Setup")
    print("=" * 60)
    print()
    
    # Check dependencies
    print("1. Checking dependencies...")
    missing = check_dependencies()
    if missing:
        print(f"❌ Missing packages: {', '.join(missing)}")
        print("   Please run: pip install -r requirements.txt")
        return False
    else:
        print("✅ All dependencies installed")
    print()
    
    # Check .env file
    print("2. Checking environment configuration...")
    env_ok, env_msg = check_env_file()
    print(env_msg)
    if not env_ok:
        print("   Please create a .env file with:")
        print("   OPENAI_API_KEY=your_api_key_here")
        return False
    print()
    
    # Create directories
    print("3. Setting up directories...")
    setup_directories()
    print("✅ Directories created")
    print()
    
    # Instructions
    print("=" * 60)
    print("Setup Complete!")
    print("=" * 60)
    print()
    print("Next steps:")
    print("1. Collect data: python data_collector.py")
    print("2. Build vector store: python vector_store.py")
    print("3. Run app: streamlit run app.py")
    print()
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)

