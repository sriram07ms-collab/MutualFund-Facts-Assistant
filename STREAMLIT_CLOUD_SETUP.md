# Streamlit Cloud Deployment - Step by Step

## 🚀 Quick Deployment Guide

### Step 1: Prepare GitHub Repository
✅ **Done!** Your code is already pushed to GitHub at:
`https://github.com/sriram07ms-collab/MutualFund-Facts-Assistant`

### Step 2: Deploy on Streamlit Cloud

1. **Go to Streamlit Cloud**
   - Visit: https://share.streamlit.io/
   - Sign in with your GitHub account (use the same account: `sriram07ms-collab`)

2. **Create New App**
   - Click "New app" button
   - Select your repository: `sriram07ms-collab/MutualFund-Facts-Assistant`
   - Branch: `main`
   - Main file path: `app.py`

3. **Configure Secrets**
   - Click "Advanced settings"
   - Under "Secrets", add:
     ```
     OPENAI_API_KEY=your_openai_api_key_here
     ```
   - Replace `your_openai_api_key_here` with your actual OpenAI API key
   - Click "Save"

4. **Deploy**
   - Click "Deploy" button
   - Wait for the app to build and deploy (2-3 minutes)

### Step 3: First Run Setup

On the first run, the app will:
1. Automatically collect data from official sources (this may take 5-10 minutes)
2. Build the vector store
3. Initialize the RAG pipeline

**Note**: The first deployment may take longer due to data collection. Subsequent runs will be faster.

### Step 4: Set Up Automated Data Refresh (Optional)

To enable daily automatic data refresh:

1. **Add GitHub Secret**
   - Go to your GitHub repository: https://github.com/sriram07ms-collab/MutualFund-Facts-Assistant
   - Click "Settings" → "Secrets and variables" → "Actions"
   - Click "New repository secret"
   - Name: `OPENAI_API_KEY`
   - Value: Your OpenAI API key
   - Click "Add secret"

2. **Enable GitHub Actions**
   - Go to "Actions" tab in your repository
   - The workflow will run automatically daily at 2 AM UTC
   - You can also trigger it manually by going to "Actions" → "Daily Data Refresh" → "Run workflow"

## 🎯 Your App URL

After deployment, your app will be available at:
```
https://[your-app-name].streamlit.app
```

## 🔧 Troubleshooting

### App Not Loading
- Check that `OPENAI_API_KEY` is set in Streamlit Cloud secrets
- Check the logs in Streamlit Cloud dashboard
- Verify all dependencies are in `requirements.txt`

### Data Collection Fails
- Check internet connectivity (Streamlit Cloud has internet access)
- Verify source URLs are accessible
- Check logs for specific errors

### Vector Store Issues
- The app will automatically rebuild the vector store on first run
- If issues persist, use the sidebar "Refresh Data & Rebuild" button

### Slow First Load
- First deployment includes data collection (5-10 minutes)
- This is normal and expected
- Subsequent loads will be faster

## 📊 Monitoring

- **Streamlit Cloud Dashboard**: Monitor app usage and logs
- **GitHub Actions**: Check data refresh status
- **App Logs**: View real-time logs in Streamlit Cloud

## 🔄 Updating the App

1. Make changes locally
2. Commit and push to GitHub:
   ```bash
   git add .
   git commit -m "Your update message"
   git push origin main
   ```
3. Streamlit Cloud will automatically redeploy

## 💡 Tips

- **Free Tier**: Streamlit Cloud free tier is sufficient for this app
- **Data Persistence**: Data persists between deployments
- **Automatic Updates**: App updates automatically on git push
- **HTTPS**: Streamlit Cloud provides free HTTPS

## 🆘 Support

If you encounter issues:
1. Check [DEPLOYMENT.md](DEPLOYMENT.md) for detailed deployment information
2. Review Streamlit Cloud logs
3. Check GitHub Actions logs for data refresh issues
4. Verify environment variables are set correctly

## ✅ Checklist

- [ ] Code pushed to GitHub ✅
- [ ] Streamlit Cloud account created
- [ ] App deployed on Streamlit Cloud
- [ ] `OPENAI_API_KEY` added to secrets
- [ ] App running successfully
- [ ] Data collection working
- [ ] GitHub Actions secret configured (optional)
- [ ] Daily data refresh enabled (optional)

## 🎉 Success!

Once deployed, your app will be live and accessible to anyone with the URL. The app will:
- Answer factual questions about mutual funds
- Provide source citations
- Refuse investment advice requests
- Update data daily (if GitHub Actions enabled)

Enjoy your deployed Mutual Fund Facts Assistant! 🚀

