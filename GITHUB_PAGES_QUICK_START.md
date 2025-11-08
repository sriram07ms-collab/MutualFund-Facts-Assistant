# 🚀 GitHub Pages Quick Start

Deploy your Mutual Fund Facts Assistant on GitHub Pages in 3 steps!

## ✅ Step 1: Enable GitHub Pages (2 minutes)

1. **Go to Repository Settings**
   - Visit: https://github.com/sriram07ms-collab/MutualFund-Facts-Assistant/settings/pages

2. **Configure Pages**
   - Under "Source", select: **GitHub Actions**
   - Click **Save**

3. **Wait for Deployment**
   - Go to **Actions** tab
   - Watch the "Deploy GitHub Pages" workflow
   - Wait 1-2 minutes

## ✅ Step 2: Access Your Site

Your site will be live at:
```
https://sriram07ms-collab.github.io/MutualFund-Facts-Assistant/
```

## ⚠️ Important: Backend API

GitHub Pages only hosts **static files**. For full chat functionality, you need to deploy the backend API separately.

### Option A: Deploy Backend on Vercel/Netlify

1. **Deploy API on Vercel or Netlify**
   - Follow: [VERCEL_DEPLOY.md](VERCEL_DEPLOY.md) or [NETLIFY_DEPLOY.md](NETLIFY_DEPLOY.md)
   - Get your API URL

2. **Update API URL in Frontend (Optional)**
   - Edit `docs/index.html`
   - Update the `API_URL` constant in the JavaScript section if you use your own backend URL
   - Commit and push

### Option B: Use Streamlit Cloud

1. **Deploy on Streamlit Cloud**
   - Go to: https://share.streamlit.io/
   - Deploy the Streamlit app
   - Link to it from GitHub Pages

## 🎉 Done!

Your GitHub Pages site is now live! 

- **Frontend**: https://sriram07ms-collab.github.io/MutualFund-Facts-Assistant/
- **Backend**: Deploy separately for full functionality

## 📚 More Help

- Full guide: [GITHUB_PAGES_DEPLOY.md](GITHUB_PAGES_DEPLOY.md)
- Vercel deployment: [VERCEL_DEPLOY.md](VERCEL_DEPLOY.md)
- Netlify deployment: [NETLIFY_DEPLOY.md](NETLIFY_DEPLOY.md)

## 🆘 Troubleshooting

### Pages Not Showing
- Check Actions tab for deployment status
- Wait 2-3 minutes after enabling
- Clear browser cache

### API Not Working
- Deploy backend on Vercel/Netlify first
- Update API URL in frontend
- Check CORS settings

Happy deploying! 🚀

