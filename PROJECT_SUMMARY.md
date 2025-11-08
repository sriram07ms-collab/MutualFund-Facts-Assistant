# Project Summary: Mutual Fund Facts Assistant

## Overview

A RAG-based FAQ assistant that answers factual questions about mutual fund schemes using verified sources from AMC, SEBI, and AMFI websites. The assistant provides concise, citation-backed responses while strictly avoiding any investment advice.

## Key Features

### ✅ Core Functionality
- **Factual Q&A**: Answers questions about expense ratios, exit loads, minimum SIP amounts, lock-in periods, riskometers, benchmarks, and statement downloads
- **Official Sources Only**: Uses only official public pages from Nippon India AMC, SEBI, and AMFI
- **Citation-Backed**: Every answer includes a source link to the official document
- **Advice Detection**: Automatically detects and refuses investment advice requests
- **Modern UI**: Clean, Groww-inspired interface for a world-class user experience

### ✅ Technical Implementation
- **RAG Pipeline**: Uses LangChain + ChromaDB for vector storage and retrieval
- **Web Scraping**: BeautifulSoup-based scraper for official sources
- **LLM Integration**: OpenAI GPT-4 for generating responses
- **Static Web UI**: Modern, responsive HTML/CSS frontend hosted on GitHub Pages

### ✅ Safety & Compliance
- **No PII Collection**: Does not accept or store personal identifiable information
- **No Investment Advice**: Strictly refuses advice requests
- **No Performance Claims**: Does not compute or compare returns
- **Transparent**: Shows source citations and last updated dates

## Project Structure

```
MutualFund-Facts-Assistant/
├── config.py              # Configuration settings
├── data_collector.py      # Web scraper for official sources
├── vector_store.py        # Vector database setup and management
├── rag_pipeline.py        # RAG pipeline for query processing
├── utils.py               # Utility functions
├── setup.py               # Setup verification script
├── test_system.py         # System testing script
├── requirements.txt       # Python dependencies
├── README.md             # Main documentation
├── QUICKSTART.md         # Quick start guide
├── PROJECT_SUMMARY.md    # This file
├── .gitignore            # Git ignore file
├── data/                 # Scraped data (gitignored)
│   └── scraped/         # Individual scraped pages
└── vector_store/         # Vector database files (gitignored)
```

## Data Sources

### Nippon India Mutual Fund (18 sources)
- Main website
- Fund pages (Large Cap, Flexi Cap, ELSS, Small Cap)
- Key Information Memorandum (KIM)
- Scheme Information Document (SID)
- NAV and Dividends
- Risk Analyzer
- And more...

### AMFI (4 sources)
- Investor Corner
- ELSS FAQs
- Risk-o-meter
- KYC information

### SEBI (2 sources)
- Investor Education
- Regulatory information

### Statement Download (2 sources)
- CAMS statements
- KFintech statements

**Total: 26 official sources**

## Workflow

1. **Data Collection**: Scrape official pages from AMC/SEBI/AMFI
2. **Text Processing**: Chunk and embed documents
3. **Vector Storage**: Store embeddings in ChromaDB
4. **Query Processing**: 
   - Check for advice requests → Refuse politely
   - Search vector store for relevant context
   - Generate factual response with LLM
   - Add source citation and timestamp
5. **Response Display**: Show answer with source link in UI

## Usage Examples

### Supported Questions
- "What is the expense ratio of Nippon India Large Cap Fund?"
- "What is the minimum SIP amount for ELSS funds?"
- "How to download capital gains statement?"
- "What is the exit load for small cap funds?"
- "What is the lock-in period for ELSS?"
- "What is the riskometer for large cap fund?"

### Refused Questions
- "Should I buy this fund?"
- "Which fund is better?"
- "What returns can I expect?"
- "Is this a good investment?"

## Setup Instructions

1. Install dependencies: `pip install -r requirements.txt`
2. Set OpenAI API key in `.env` file
3. Collect data: `python data_collector.py`
4. Build vector store: `python vector_store.py`
5. Open the web UI: launch a simple HTTP server and visit `http://localhost:8080/docs/index.html`

See [QUICKSTART.md](QUICKSTART.md) for detailed instructions.

## Configuration

Key configuration options in `config.py`:
- `CHUNK_SIZE`: Text chunk size for embeddings (1000)
- `CHUNK_OVERLAP`: Overlap between chunks (200)
- `EMBEDDING_MODEL`: OpenAI embedding model
- `LLM_MODEL`: OpenAI LLM model (GPT-4)
- `TOP_K_RESULTS`: Number of search results to use (3)
- `ADVICE_KEYWORDS`: Keywords to detect advice requests

## Testing

Run system tests:
```bash
python test_system.py
```

This will verify:
- All dependencies are installed
- Environment variables are set
- Data collection is complete
- Vector store is built
- RAG pipeline can be initialized

## Future Enhancements

Possible extensions:
- Add more AMCs and schemes
- Support for PDF document parsing
- Multi-language support
- Advanced search filters
- Export conversation history
- Integration with official APIs

## License & Disclaimer

This project is for educational and informational purposes only. It does not provide investment advice.

**MUTUAL FUND INVESTMENTS ARE SUBJECT TO MARKET RISKS. READ ALL SCHEME RELATED DOCUMENTS CAREFULLY.**

## Support

For issues or questions:
- Check [README.md](README.md) for documentation
- See [QUICKSTART.md](QUICKSTART.md) for setup help
- Verify official sources: [Nippon India MF](https://mf.nipponindiaim.com/), [AMFI](https://www.amfiindia.com/), [SEBI](https://www.sebi.gov.in/)

