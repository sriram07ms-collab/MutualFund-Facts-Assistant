# Deployment Guide

This guide explains how to deploy the Mutual Fund Facts Assistant to production with real-time data.

## Deployment Options

### Option 1: Streamlit Cloud (Recommended - Free)

Streamlit Cloud is the easiest way to deploy Streamlit apps for free.

#### Steps:

1. **Push code to GitHub** (already done)
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Deploy on Streamlit Cloud**:
   - Go to [https://share.streamlit.io/](https://share.streamlit.io/)
   - Sign in with your GitHub account
   - Click "New app"
   - Select your repository: `sriram07ms-collab/MutualFund-Facts-Assistant`
   - Set main file path: `app.py`
   - Add secrets (see Environment Variables section below)
   - Click "Deploy"

3. **Configure Environment Variables**:
   - In Streamlit Cloud, go to App settings → Secrets
   - Add:
     ```
     OPENAI_API_KEY=your_openai_api_key_here
     ```

4. **Set up Data Refresh**:
   - The app will automatically collect data on first run
   - For scheduled updates, use GitHub Actions (see below)

#### Streamlit Cloud Advantages:
- ✅ Free for public repos
- ✅ Automatic HTTPS
- ✅ Easy deployment
- ✅ Built-in secret management
- ✅ Automatic updates on git push

### Option 2: Railway.app

Railway is a modern deployment platform with good free tier.

#### Steps:

1. **Install Railway CLI**:
   ```bash
   npm i -g @railway/cli
   railway login
   ```

2. **Deploy**:
   ```bash
   railway init
   railway up
   ```

3. **Set Environment Variables**:
   ```bash
   railway variables set OPENAI_API_KEY=your_key
   ```

### Option 3: Render.com

Render offers free tier with some limitations.

#### Steps:

1. Connect your GitHub repository to Render
2. Create a new Web Service
3. Set build command: `pip install -r requirements.txt && python data_collector.py && python vector_store.py`
4. Set start command: `streamlit run app.py --server.port=$PORT --server.address=0.0.0.0`
5. Add environment variables in Render dashboard

## Automated Data Refresh

### Using GitHub Actions

The repository includes a GitHub Actions workflow (`.github/workflows/data-refresh.yml`) that:
- Runs daily at 2 AM UTC
- Collects fresh data from official sources
- Rebuilds the vector store
- Commits updates to the repository

#### Setup:

1. **Add GitHub Secret**:
   - Go to repository Settings → Secrets and variables → Actions
   - Add secret: `OPENAI_API_KEY` with your API key

2. **Enable Workflow**:
   - The workflow is already configured
   - It will run automatically on the schedule
   - You can also trigger it manually from Actions tab

### Manual Data Refresh

Users can refresh data from the app's sidebar:
- Click "🔄 Refresh Data & Rebuild" button
- The app will collect fresh data and rebuild the vector store

## Environment Variables

Required environment variables:

```bash
OPENAI_API_KEY=your_openai_api_key_here
```

Optional variables (can be set in `config.py`):
- `EMBEDDING_MODEL` - Default: `text-embedding-3-small`
- `LLM_MODEL` - Default: `gpt-4-turbo-preview`
- `CHUNK_SIZE` - Default: `1000`
- `CHUNK_OVERLAP` - Default: `200`

## Data Storage

### For Streamlit Cloud:
- Data is stored in the app's file system
- Data persists between deployments
- Vector store is rebuilt on each deployment (or use GitHub Actions to update)

### For Other Platforms:
- Consider using cloud storage (S3, Google Cloud Storage) for data files
- Use managed vector databases (Pinecone, Weaviate) for production
- Update `vector_store.py` to use cloud storage

## Production Considerations

### 1. Data Persistence
- For production, store data in cloud storage (S3, GCS)
- Use managed vector databases (Pinecone, Weaviate, Qdrant)
- Update code to fetch from cloud storage on startup

### 2. Caching
- Add caching for frequent queries
- Use Redis or similar for response caching
- Cache vector store searches

### 3. Rate Limiting
- Implement rate limiting for API calls
- Add request throttling
- Monitor API usage

### 4. Monitoring
- Add logging and error tracking
- Monitor OpenAI API usage
- Track user queries and responses

### 5. Scaling
- Use load balancer for multiple instances
- Consider async processing for data collection
- Use message queue for background tasks

## Troubleshooting

### Data Collection Fails
- Check internet connectivity
- Verify source URLs are accessible
- Check rate limiting on source websites
- Review error logs

### Vector Store Issues
- Ensure sufficient disk space
- Check ChromaDB version compatibility
- Verify embeddings are generated correctly

### Deployment Issues
- Check environment variables are set
- Verify all dependencies are in requirements.txt
- Check build logs for errors
- Ensure Python version is compatible

## Updating the App

1. **Make changes locally**
2. **Test locally**: `streamlit run app.py`
3. **Commit and push**:
   ```bash
   git add .
   git commit -m "Update: description of changes"
   git push origin main
   ```
4. **Deploy automatically** (Streamlit Cloud) or manually trigger deployment

## Support

For deployment issues:
- Check [Streamlit Cloud documentation](https://docs.streamlit.io/streamlit-community-cloud)
- Review deployment logs
- Check GitHub Actions logs for data refresh issues

