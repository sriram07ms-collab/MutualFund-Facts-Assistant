"""
Configuration file for Mutual Fund Facts Assistant
"""
import os
from pathlib import Path

# Project paths
PROJECT_ROOT = Path(__file__).parent
DATA_DIR = PROJECT_ROOT / "data"
VECTOR_STORE_DIR = PROJECT_ROOT / "vector_store"
SCRAPED_DATA_DIR = DATA_DIR / "scraped"

# Create directories if they don't exist
DATA_DIR.mkdir(exist_ok=True)
VECTOR_STORE_DIR.mkdir(exist_ok=True)
SCRAPED_DATA_DIR.mkdir(exist_ok=True)

# URLs to scrape
SOURCE_URLS = {
    "nippon_main": "https://mf.nipponindiaim.com/",
    "large_cap": "https://mf.nipponindiaim.com/funds-and-plans/equity-funds/nippon-india-large-cap-fund",
    "flexi_cap": "https://mf.nipponindiaim.com/funds-and-plans/equity-funds/nippon-india-flexi-cap-fund",
    "elss": "https://mf.nipponindiaim.com/funds-and-plans/equity-funds/nippon-india-elss-tax-saver-fund",
    "small_cap": "https://mf.nipponindiaim.com/FundsAndPerformance/Pages/NipponIndia-Small-Cap-Fund.aspx",
    "by_asset_class": "https://mf.nipponindiaim.com/our-products/by-asset-class/",
    "kim": "https://mf.nipponindiaim.com/investor-services/forms-and-downloads/key-information-memorandum",
    "sid": "https://mf.nipponindiaim.com/investor-services/forms-and-downloads/scheme-information-document",
    "addenda": "https://mf.nipponindiaim.com/investor-services/forms-and-downloads/addenda-and-notices",
    "nav_dividends": "https://mf.nipponindiaim.com/investor-services/nav-and-dividends",
    "amfi_investor": "https://www.amfiindia.com/investor-corner",
    "amfi_elss_faq": "https://www.amfiindia.com/investor-corner/knowledge-center/faqs#elss",
    "amfi_riskometer": "https://www.amfiindia.com/investor-corner/knowledge-center/risk-o-meter",
    "sebi_education": "https://investor.sebi.gov.in/investor_education.html",
    "sebi_home": "https://www.sebi.gov.in/sebiweb/home/HomeAction.do?doListing=yes&sid=3",
    "cams_statements": "https://new.camsonline.com/Investors/Statements/Consolidated-Account-Statement",
    "kfintech_statements": "https://mfs.kfintech.com/investor/General/Download-Statements",
    "amfi_kyc": "https://www.amfiindia.com/investor-corner/knowledge-center/kyc",
    "risk_analyzer": "https://mf.nipponindiaim.com/knowledge-center/tools/risk-analyzer"
}

# RAG Configuration
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200
EMBEDDING_MODEL = "text-embedding-3-small"
LLM_MODEL = "gpt-4-turbo-preview"
TEMPERATURE = 0.1
MAX_TOKENS = 300

# Vector Store Configuration
COLLECTION_NAME = "mutual_fund_facts"
TOP_K_RESULTS = 3

# UI Configuration
APP_TITLE = "Mutual Fund Facts Assistant"
APP_SUBTITLE = "Get factual answers about mutual fund schemes"
EXAMPLE_QUESTIONS = [
    "What is the expense ratio of Nippon India Large Cap Fund?",
    "What is the minimum SIP amount for ELSS funds?",
    "How to download capital gains statement?"
]

# Advice detection keywords
ADVICE_KEYWORDS = [
    "should i", "should i buy", "should i sell", "is it good", "is it bad",
    "recommend", "best", "worst", "compare returns", "which is better",
    "advice", "suggest", "opinion", "think", "believe"
]

# Response templates
ADVICE_REFUSAL_MESSAGE = """I can only provide factual information from official sources. For investment advice, please consult a registered investment advisor or financial planner.

You can learn more about mutual funds at: https://www.amfiindia.com/investor-corner/knowledge-center/faqs"""

