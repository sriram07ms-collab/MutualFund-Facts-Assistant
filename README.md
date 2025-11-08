# Mutual Fund Facts Assistant

A RAG-based FAQ assistant that answers factual questions about mutual fund schemes using verified sources from AMC, SEBI, and AMFI websites. Provides concise, citation-backed responses while strictly avoiding any investment advice.

## Features

- ✅ **Factual Information Only**: Answers questions about expense ratios, exit loads, minimum SIP amounts, lock-in periods, riskometers, benchmarks, and statement downloads
- ✅ **Official Sources**: Uses only official public pages from Nippon India AMC, SEBI, and AMFI
- ✅ **Citation-Backed**: Every answer includes a source link to the official document
- ✅ **Advice Detection**: Automatically detects and refuses investment advice requests
- ✅ **Modern UI**: Clean, Groww-inspired interface for a world-class user experience
- ✅ **No PII Collection**: Does not accept or store any personal identifiable information

## Scope

This assistant covers:
- **AMC**: Nippon India Mutual Fund
- **Schemes**: 
  - Large Cap Fund
  - Flexi Cap Fund
  - ELSS Tax Saver Fund
  - Small Cap Fund

## 🚀 Quick Deploy

### Option 1: Vercel (Recommended - Full Stack)

**Deploy on Vercel (Free):**
1. Go to [vercel.com](https://vercel.com/)
2. Sign in with GitHub
3. Import repository: `sriram07ms-collab/MutualFund-Facts-Assistant`
4. Set environment variable: `OPENAI_API_KEY`
5. Deploy!

See [VERCEL_DEPLOY.md](VERCEL_DEPLOY.md) for detailed instructions.

### Option 2: Netlify (Recommended - Full Stack)

**Deploy on Netlify (Free):**
1. Go to [netlify.com](https://app.netlify.com/)
2. Sign in with GitHub
3. Import repository: `sriram07ms-collab/MutualFund-Facts-Assistant`
4. Set environment variable: `OPENAI_API_KEY`
5. Deploy!

See [NETLIFY_DEPLOY.md](NETLIFY_DEPLOY.md) for detailed instructions.

### Option 3: GitHub Pages + Streamlit Cloud

**Deploy landing page on GitHub Pages:**
1. Go to repository Settings → Pages
2. Select "GitHub Actions" as source
3. The landing page will deploy automatically

**Deploy app on Streamlit Cloud:**
1. Go to [share.streamlit.io](https://share.streamlit.io/)
2. Connect your GitHub account
3. Select this repository
4. Add your `OPENAI_API_KEY` in Secrets
5. Click Deploy!

See [GITHUB_PAGES_SETUP.md](GITHUB_PAGES_SETUP.md) for detailed instructions.

## Setup (Local Development)

### Prerequisites

- Python 3.8 or higher
- OpenAI API key ([Get one here](https://platform.openai.com/api-keys))

### Quick Installation

1. **Clone the repository:**
```bash
git clone <repository-url>
cd MutualFund-Facts-Assistant
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Set up environment variables:**
Create a `.env` file in the project root:
```bash
OPENAI_API_KEY=your_api_key_here
```

4. **Verify setup (optional):**
```bash
python test_system.py
```

5. **Collect data from official sources:**
```bash
python data_collector.py
```

6. **Build the vector store:**
```bash
python vector_store.py
```

7. **Run the Streamlit app:**
```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

### Alternative: Using Setup Script

```bash
python setup.py
```

This will check your installation and guide you through the setup process.

For detailed step-by-step instructions, see [QUICKSTART.md](QUICKSTART.md)

## Usage

### Example Questions

- "What is the expense ratio of Nippon India Large Cap Fund?"
- "What is the minimum SIP amount for ELSS funds?"
- "How to download capital gains statement?"
- "What is the exit load for small cap funds?"
- "What is the lock-in period for ELSS?"

### What the Assistant Does

✅ Provides factual information from official sources
✅ Includes source citations in every answer
✅ Refuses investment advice requests politely
✅ Keeps answers concise (1-3 sentences)

### What the Assistant Doesn't Do

❌ Provide investment advice or recommendations
❌ Compare fund performance or returns
❌ Accept or store personal information (PAN, Aadhaar, etc.)
❌ Make predictions about future performance

## Project Structure

```
MutualFund-Facts-Assistant/
├── app.py                  # Streamlit UI application
├── config.py              # Configuration settings
├── data_collector.py      # Web scraper for official sources
├── vector_store.py        # Vector database setup and management
├── rag_pipeline.py        # RAG pipeline for query processing
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variables template
├── .gitignore            # Git ignore file
├── README.md             # This file
├── data/                 # Scraped data (gitignored)
│   └── scraped/         # Individual scraped pages
└── vector_store/         # Vector database files (gitignored)
```

## Data Sources

The assistant uses the following official sources:

### Nippon India Mutual Fund
- Main website
- Fund pages (Large Cap, Flexi Cap, ELSS, Small Cap)
- Key Information Memorandum (KIM)
- Scheme Information Document (SID)
- NAV and Dividends
- Risk Analyzer

### AMFI
- Investor Corner
- ELSS FAQs
- Risk-o-meter
- KYC information

### SEBI
- Investor Education
- Regulatory information

### Statement Download
- CAMS statements
- KFintech statements

## Configuration

Edit `config.py` to customize:
- Chunk size and overlap for text splitting
- Embedding and LLM models
- Vector store settings
- UI configuration
- Advice detection keywords

## Key Constraints

1. **Public Sources Only**: No third-party blogs or unofficial sources
2. **No PII**: Does not accept PAN, Aadhaar, account numbers, OTPs, emails, or phone numbers
3. **No Performance Claims**: Does not compute or compare returns
4. **Factual Only**: Answers are limited to 3 sentences with source citations

## Troubleshooting

### Vector Store Not Found
- Run `python data_collector.py` to collect data
- Run `python vector_store.py` to build the vector store

### OpenAI API Error
- Check that your API key is set correctly in `.env`
- Ensure you have sufficient API credits

### No Results Found
- The query might not be in the scraped sources
- Try rephrasing the question
- Check if the source URLs are still accessible

## License

This project is for educational and informational purposes only. It does not provide investment advice.

## Disclaimer

MUTUAL FUND INVESTMENTS ARE SUBJECT TO MARKET RISKS. READ ALL SCHEME RELATED DOCUMENTS CAREFULLY. This assistant provides factual information only and does not constitute investment advice. Always consult a registered investment advisor before making investment decisions.

## Deployment

This app can be deployed to:
- **Streamlit Cloud** (Recommended - Free): See [DEPLOYMENT.md](DEPLOYMENT.md)
- **Railway.app**: Modern deployment platform
- **Render.com**: Free tier available

For detailed deployment instructions, see [DEPLOYMENT.md](DEPLOYMENT.md).

## Automated Data Refresh

The repository includes GitHub Actions workflow for automatic daily data refresh:
- Runs daily at 2 AM UTC
- Collects fresh data from official sources
- Rebuilds vector store
- Updates repository automatically

See `.github/workflows/data-refresh.yml` for configuration.

## Support

For issues or questions:
- Check the [README.md](README.md) for detailed documentation
- See [DEPLOYMENT.md](DEPLOYMENT.md) for deployment help
- Verify official sources: [Nippon India MF](https://mf.nipponindiaim.com/), [AMFI](https://www.amfiindia.com/), [SEBI](https://www.sebi.gov.in/)

