# Quick Start Guide

## Prerequisites

- Python 3.8 or higher
- OpenAI API key ([Get one here](https://platform.openai.com/api-keys))

## Installation & Setup

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 2: Configure Environment

Create a `.env` file in the project root:

```bash
OPENAI_API_KEY=your_openai_api_key_here
```

### Step 3: Run Setup (Optional)

```bash
python setup.py
```

This will check your installation and configuration.

### Step 4: Collect Data

Collect data from official sources:

```bash
python data_collector.py
```

This will scrape official pages from:
- Nippon India Mutual Fund website
- AMFI website
- SEBI website

### Step 5: Build Vector Store

Build the vector database:

```bash
python vector_store.py
```

### Step 6: Run the App

Start the Streamlit application:

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## Usage

### Example Questions You Can Ask

1. **Expense Ratio**
   - "What is the expense ratio of Nippon India Large Cap Fund?"
   - "What is the expense ratio for ELSS funds?"

2. **SIP Information**
   - "What is the minimum SIP amount?"
   - "What is the minimum investment for SIP?"

3. **Exit Load**
   - "What is the exit load for small cap funds?"
   - "Exit load for flexi cap fund?"

4. **Lock-in Period**
   - "What is the lock-in period for ELSS?"
   - "ELSS lock-in period?"

5. **Riskometer**
   - "What is the riskometer for large cap fund?"
   - "Risk rating of ELSS fund?"

6. **Benchmark**
   - "What is the benchmark for Nippon India Large Cap Fund?"
   - "Benchmark index for small cap fund?"

7. **Statements**
   - "How to download capital gains statement?"
   - "How to download account statement?"
   - "Where can I download my mutual fund statement?"

### What the Assistant Does

✅ Answers factual questions from official sources
✅ Provides source citations for every answer
✅ Refuses investment advice requests politely
✅ Keeps answers concise and clear

### What the Assistant Doesn't Do

❌ Provide investment advice or recommendations
❌ Compare fund performance
❌ Make predictions about future returns
❌ Accept personal information (PAN, Aadhaar, etc.)

## Troubleshooting

### "Vector store not found" Error

Run data collection and vector store build:
```bash
python data_collector.py
python vector_store.py
```

### "OpenAI API key not found" Error

Make sure you have created a `.env` file with your API key:
```bash
OPENAI_API_KEY=sk-your-key-here
```

### "No results found" Error

- Try rephrasing your question
- Check if the information is available in the official sources
- The data might need to be refreshed - use the sidebar button

### Data Collection Issues

- Check your internet connection
- Some websites may have rate limiting - wait a few minutes and try again
- Verify that the source URLs are still accessible

## Refreshing Data

To update the data from official sources:

1. Use the sidebar button "🔄 Refresh Data & Rebuild" in the app, OR
2. Run the commands again:
   ```bash
   python data_collector.py
   python vector_store.py
   ```

## Support

For issues or questions:
- Check the [README.md](README.md) for detailed documentation
- Verify official sources: [Nippon India MF](https://mf.nipponindiaim.com/), [AMFI](https://www.amfiindia.com/), [SEBI](https://www.sebi.gov.in/)

## Next Steps

- Customize the configuration in `config.py`
- Add more schemes or sources
- Extend the question types handled

