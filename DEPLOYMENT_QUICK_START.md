# 🚀 Quick Deployment Guide

Choose your preferred platform and deploy in minutes!

## 📋 Prerequisites

- GitHub repository: `sriram07ms-collab/MutualFund-Facts-Assistant` ✅
- OpenAI API key: [Get one here](https://platform.openai.com/api-keys)

## 🎯 Deployment Options

### Option 1: Vercel (Recommended) ⚡

**Best for**: Full-stack deployment with serverless functions

1. **Go to Vercel**
   - Visit: https://vercel.com/
   - Sign in with GitHub

2. **Import Project**
   - Click "Add New Project"
   - Select repository: `sriram07ms-collab/MutualFund-Facts-Assistant`
   - Click "Import"

3. **Configure**
   - Framework Preset: **Other**
   - Root Directory: `./`
   - Build Command: (leave empty)
   - Output Directory: `public`

4. **Set Environment Variables**
   - Click "Environment Variables"
   - Add: `OPENAI_API_KEY` = your API key
   - Click "Save"

5. **Deploy**
   - Click "Deploy"
   - Wait 2-3 minutes
   - Your app: `https://your-project.vercel.app`

**Detailed guide**: [VERCEL_DEPLOY.md](VERCEL_DEPLOY.md)

---

### Option 2: Netlify 🚀

**Best for**: Full-stack deployment with serverless functions

1. **Go to Netlify**
   - Visit: https://app.netlify.com/
   - Sign in with GitHub

2. **Add New Site**
   - Click "Add new site" → "Import an existing project"
   - Select "GitHub"
   - Select repository: `sriram07ms-collab/MutualFund-Facts-Assistant`

3. **Configure**
   - Build command: (leave empty)
   - Publish directory: `public`

4. **Set Environment Variables**
   - Click "Show advanced"
   - Add: `OPENAI_API_KEY` = your API key
   - Click "Save"

5. **Deploy**
   - Click "Deploy site"
   - Wait 2-3 minutes
   - Your app: `https://your-site.netlify.app`

**Detailed guide**: [NETLIFY_DEPLOY.md](NETLIFY_DEPLOY.md)

---

### Option 3: GitHub Pages + Streamlit Cloud 📄

**Best for**: Separate landing page and app

1. **GitHub Pages**
   - Go to repository Settings → Pages
   - Source: GitHub Actions
   - Landing page: `https://sriram07ms-collab.github.io/MutualFund-Facts-Assistant/`

2. **Streamlit Cloud**
   - Go to: https://share.streamlit.io/
   - Sign in with GitHub
   - Import repository
   - Add `OPENAI_API_KEY` in secrets
   - Deploy

**Detailed guide**: [GITHUB_PAGES_SETUP.md](GITHUB_PAGES_SETUP.md)

---

## ⚙️ Setup After Deployment

### First Request

The first API request will:
1. Collect data from official sources (5-10 minutes)
2. Build vector store
3. Process your query

**Note**: This is a one-time setup. Subsequent requests will be faster.

### Environment Variables

Required:
- `OPENAI_API_KEY` - Your OpenAI API key

Optional:
- `EMBEDDING_MODEL` - Default: `text-embedding-3-small`
- `LLM_MODEL` - Default: `gpt-4-turbo-preview`

## 🎨 Features

- ✅ Beautiful chat interface
- ✅ Real-time query processing
- ✅ Source citations
- ✅ Advice detection
- ✅ Mobile responsive
- ✅ Free hosting

## 🐛 Troubleshooting

### API Not Working

1. Check environment variables are set
2. Check function logs in dashboard
3. Verify OpenAI API key is valid
4. Wait for first request to complete (data collection)

### Slow First Response

- **Normal**: First request takes 5-10 minutes
- This is for data collection and vector store building
- Subsequent requests are fast

### Vector Store Issues

- The system will auto-initialize on first request
- If issues persist, check function logs
- Verify data collection is working

## 📊 Comparison

| Platform | Pros | Cons |
|----------|------|------|
| **Vercel** | Fast, great DX, auto-deploy | Serverless timeout limits |
| **Netlify** | Easy setup, good free tier | Serverless timeout limits |
| **Streamlit Cloud** | Native Streamlit support | Separate from GitHub Pages |

## ✅ Checklist

- [ ] Code pushed to GitHub
- [ ] Platform account created
- [ ] Repository imported
- [ ] Environment variables set
- [ ] App deployed
- [ ] First request completed
- [ ] App working correctly

## 🎉 Success!

Once deployed, you'll have:
- ✅ Full-stack web application
- ✅ Serverless API backend
- ✅ Beautiful frontend
- ✅ Real-time data updates
- ✅ Free hosting

## 📚 More Help

- Vercel: [VERCEL_DEPLOY.md](VERCEL_DEPLOY.md)
- Netlify: [NETLIFY_DEPLOY.md](NETLIFY_DEPLOY.md)
- GitHub Pages: [GITHUB_PAGES_SETUP.md](GITHUB_PAGES_SETUP.md)
- General: [DEPLOYMENT.md](DEPLOYMENT.md)

## 🆘 Support

For issues:
1. Check deployment platform logs
2. Verify environment variables
3. Check function logs
4. Review deployment documentation

Happy deploying! 🚀

