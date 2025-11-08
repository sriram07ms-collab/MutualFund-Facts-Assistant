# Netlify Deployment Guide

This guide explains how to deploy the Mutual Fund Facts Assistant on Netlify.

## 🚀 Quick Deploy

### Option 1: Deploy with Netlify CLI

1. **Install Netlify CLI**
   ```bash
   npm install -g netlify-cli
   ```

2. **Login to Netlify**
   ```bash
   netlify login
   ```

3. **Deploy**
   ```bash
   netlify deploy --prod
   ```

4. **Follow the prompts**
   - Link to existing site or create new
   - Set environment variables

### Option 2: Deploy via GitHub (Recommended)

1. **Push code to GitHub**
   - Your code is already on GitHub

2. **Go to Netlify**
   - Visit: https://app.netlify.com/
   - Sign in with GitHub

3. **Add New Site**
   - Click "Add new site" → "Import an existing project"
   - Select "GitHub"
   - Authorize Netlify
   - Select repository: `sriram07ms-collab/MutualFund-Facts-Assistant`
   - Click "Import"

4. **Configure Build Settings**
   - Build command: (leave empty)
   - Publish directory: `public`
   - Click "Show advanced"
   - Add environment variables:
     - `OPENAI_API_KEY` = your OpenAI API key

5. **Deploy**
   - Click "Deploy site"
   - Wait for deployment to complete

## 📋 Project Structure

```
MutualFund-Facts-Assistant/
├── public/                    # Static files (HTML, CSS, JS)
│   └── index.html            # Main frontend
├── netlify/                  # Netlify functions
│   └── functions/
│       └── query.py          # RAG query handler
├── netlify.toml              # Netlify configuration
└── requirements.txt          # Python dependencies
```

## ⚙️ Configuration

### Environment Variables

Required:
- `OPENAI_API_KEY` - Your OpenAI API key

Optional:
- `EMBEDDING_MODEL` - Default: `text-embedding-3-small`
- `LLM_MODEL` - Default: `gpt-4-turbo-preview`

### Netlify Configuration

The `netlify.toml` file configures:
- Build settings
- Function directory
- Python plugin
- Publishing directory

## 🔧 Setup Data and Vector Store

**Important**: The vector store needs to be initialized before the API can work.

### Option 1: Initialize on First Request (Recommended)

The API will automatically:
1. Check if vector store exists
2. Collect data if needed
3. Build vector store
4. Process queries

**Note**: First request may take 5-10 minutes for data collection.

### Option 2: Pre-initialize (Advanced)

1. **Run data collection locally**
   ```bash
   python data_collector.py
   python vector_store.py
   ```

2. **Upload data to Netlify**
   - Use Netlify Large Media or
   - Include data files in deployment (not recommended for large files)

3. **Update API to use cloud storage**
   - Modify `netlify/functions/query.py` to fetch from cloud storage

## 📊 API Endpoint

### POST `/.netlify/functions/query`

**Request:**
```json
{
  "query": "What is the expense ratio of Nippon India Large Cap Fund?"
}
```

**Response:**
```json
{
  "answer": "The expense ratio of Nippon India Large Cap Fund is...",
  "source": "https://mf.nipponindiaim.com/...",
  "is_advice": false
}
```

## 🐛 Troubleshooting

### API Returns 500 Error

1. **Check Environment Variables**
   - Go to Site settings → Environment variables
   - Verify `OPENAI_API_KEY` is set
   - Check function logs in Netlify dashboard

2. **Check Vector Store**
   - First request may take time to initialize
   - Check function logs for errors
   - Verify data collection is working

3. **Check Function Logs**
   - Go to Netlify dashboard
   - Click on your site
   - Go to "Functions" tab
   - View logs for `query` function

### Slow First Response

- **Expected**: First request takes 5-10 minutes
- This is normal for initial data collection and vector store building
- Subsequent requests will be faster

### CORS Errors

- CORS is already configured in the API
- If issues persist, check function logs
- Verify headers are set correctly

### Vector Store Not Found

1. **Check if data directory exists**
2. **Run data collection** (may need to do this locally first)
3. **Update API** to handle missing vector store gracefully

## 🔄 Updating the App

1. **Make changes locally**
2. **Commit and push to GitHub**
   ```bash
   git add .
   git commit -m "Update app"
   git push origin main
   ```
3. **Netlify automatically redeploys**
   - Go to Netlify dashboard to see deployment status

## 💡 Tips

- **Free Tier**: Netlify free tier is sufficient for this app
- **Serverless Functions**: Each function has timeout limits
- **Cold Starts**: First request after inactivity may be slower
- **Environment Variables**: Set in Netlify dashboard, not in code
- **Python Plugin**: Netlify automatically installs Python dependencies

## 📚 Resources

- [Netlify Documentation](https://docs.netlify.com/)
- [Netlify Functions](https://docs.netlify.com/functions/overview/)
- [Netlify Python Functions](https://docs.netlify.com/functions/create-functions/python/)

## ✅ Checklist

- [ ] Code pushed to GitHub
- [ ] Netlify account created
- [ ] Site imported from GitHub
- [ ] Environment variables set
- [ ] Site deployed successfully
- [ ] API endpoint working
- [ ] Frontend accessible
- [ ] Vector store initialized

## 🎉 Success!

Once deployed, your app will be available at:
```
https://your-site-name.netlify.app
```

The app includes:
- ✅ Beautiful frontend interface
- ✅ Serverless API backend
- ✅ RAG pipeline for query processing
- ✅ Real-time data updates
- ✅ Source citations

Enjoy your deployed Mutual Fund Facts Assistant! 🚀

