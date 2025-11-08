# Vercel Deployment Guide

This guide explains how to deploy the Mutual Fund Facts Assistant on Vercel.

## 🚀 Quick Deploy

### Option 1: Deploy with Vercel CLI

1. **Install Vercel CLI**
   ```bash
   npm i -g vercel
   ```

2. **Login to Vercel**
   ```bash
   vercel login
   ```

3. **Deploy**
   ```bash
   vercel
   ```

4. **Follow the prompts**
   - Link to existing project or create new
   - Set environment variables when prompted

### Option 2: Deploy via GitHub (Recommended)

1. **Push code to GitHub**
   - Your code is already on GitHub

2. **Go to Vercel**
   - Visit: https://vercel.com/
   - Sign in with GitHub

3. **Import Project**
   - Click "Add New Project"
   - Select your repository: `sriram07ms-collab/MutualFund-Facts-Assistant`
   - Click "Import"

4. **Configure Project**
   - Framework Preset: Other
   - Root Directory: `./`
   - Build Command: (leave empty)
   - Output Directory: `public`

5. **Set Environment Variables**
   - Click "Environment Variables"
   - Add:
     - `OPENAI_API_KEY` = your OpenAI API key
   - Click "Save"

6. **Deploy**
   - Click "Deploy"
   - Wait for deployment to complete

## 📋 Project Structure

```
MutualFund-Facts-Assistant/
├── public/              # Static files (HTML, CSS, JS)
│   └── index.html      # Main frontend
├── api/                # Serverless functions
│   └── query.py        # RAG query handler
├── vercel.json         # Vercel configuration
└── requirements.txt    # Python dependencies
```

## ⚙️ Configuration

### Environment Variables

Required:
- `OPENAI_API_KEY` - Your OpenAI API key

Optional:
- `EMBEDDING_MODEL` - Default: `text-embedding-3-small`
- `LLM_MODEL` - Default: `gpt-4-turbo-preview`

### Vercel Configuration

The `vercel.json` file configures:
- Python serverless functions
- Static file serving
- API routes
- Function timeout (30 seconds)

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

2. **Upload data to Vercel**
   - Use Vercel Blob Storage or
   - Include data files in deployment (not recommended for large files)

3. **Update API to use cloud storage**
   - Modify `api/query.py` to fetch from cloud storage

## 📊 API Endpoint

### POST `/api/query`

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
   - Verify `OPENAI_API_KEY` is set in Vercel dashboard
   - Check function logs in Vercel dashboard

2. **Check Vector Store**
   - First request may take time to initialize
   - Check function logs for errors
   - Verify data collection is working

3. **Check Function Logs**
   - Go to Vercel dashboard
   - Click on your project
   - Go to "Functions" tab
   - View logs for `/api/query`

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
3. **Vercel automatically redeploys**
   - Go to Vercel dashboard to see deployment status

## 💡 Tips

- **Free Tier**: Vercel free tier is sufficient for this app
- **Serverless Functions**: Each function has a 30-second timeout (configurable)
- **Cold Starts**: First request after inactivity may be slower
- **Environment Variables**: Set in Vercel dashboard, not in code

## 📚 Resources

- [Vercel Documentation](https://vercel.com/docs)
- [Vercel Python Support](https://vercel.com/docs/concepts/functions/serverless-functions/runtimes/python)
- [Vercel Serverless Functions](https://vercel.com/docs/concepts/functions/serverless-functions)

## ✅ Checklist

- [ ] Code pushed to GitHub
- [ ] Vercel account created
- [ ] Project imported from GitHub
- [ ] Environment variables set
- [ ] Project deployed successfully
- [ ] API endpoint working
- [ ] Frontend accessible
- [ ] Vector store initialized

## 🎉 Success!

Once deployed, your app will be available at:
```
https://your-project-name.vercel.app
```

The app includes:
- ✅ Beautiful frontend interface
- ✅ Serverless API backend
- ✅ RAG pipeline for query processing
- ✅ Real-time data updates
- ✅ Source citations

Enjoy your deployed Mutual Fund Facts Assistant! 🚀

