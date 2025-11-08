# GitHub Pages Deployment Guide

This guide explains how to deploy the Mutual Fund Facts Assistant frontend on GitHub Pages.

## 🚀 Quick Deploy

### Step 1: Enable GitHub Pages

1. **Go to Repository Settings**
   - Visit: https://github.com/sriram07ms-collab/MutualFund-Facts-Assistant/settings/pages

2. **Configure GitHub Pages**
   - Under "Source", select: **GitHub Actions**
   - Click **Save**

3. **Verify Deployment**
   - Go to **Actions** tab
   - You'll see "Deploy GitHub Pages" workflow running
   - Wait 1-2 minutes for deployment to complete

4. **Access Your Site**
   - Your site will be live at:
     ```
     https://sriram07ms-collab.github.io/MutualFund-Facts-Assistant/
     ```

## ⚠️ Important Note

GitHub Pages only hosts **static files** (HTML, CSS, JavaScript). The chat functionality requires a backend API, which cannot run on GitHub Pages.

### Options for Full Functionality

1. **Deploy Backend Separately**
   - Deploy API on Vercel or Netlify
   - Update API URL in the frontend
   - Full functionality available

2. **Use Streamlit Cloud**
   - Deploy full Streamlit app on Streamlit Cloud
   - Link to it from GitHub Pages
   - Complete solution

3. **Use Vercel/Netlify for Full Stack**
   - Deploy both frontend and backend together
   - Single deployment
   - Recommended for production

## 🔧 Configuring API Endpoint

### Option 1: Update in HTML (For GitHub Pages)

Edit `docs/index.html` and update the API URL:

```javascript
const API_URL = 'https://your-vercel-app.vercel.app/api/query';
// or
const API_URL = 'https://your-netlify-app.netlify.app/.netlify/functions/query';
```

### Option 2: Use Environment Variable (For Vercel/Netlify)

Set environment variable in deployment platform:
- `API_URL` = your API endpoint URL

## 📋 Project Structure

```
MutualFund-Facts-Assistant/
├── docs/
│   └── index.html          # GitHub Pages frontend
├── public/
│   └── index.html          # Vercel/Netlify frontend
├── api/
│   └── query.py            # Vercel serverless function
├── netlify/
│   └── functions/
│       └── query.py        # Netlify serverless function
└── .github/workflows/
    └── pages.yml           # GitHub Pages deployment workflow
```

## 🎯 Deployment Workflow

The GitHub Actions workflow (`.github/workflows/pages.yml`) automatically:
1. Deploys on every push to `main` branch
2. Builds and deploys the `docs/` directory
3. Makes it available on GitHub Pages

## 🔄 Updating the Site

1. **Make changes** to `docs/index.html`
2. **Commit and push** to GitHub:
   ```bash
   git add docs/index.html
   git commit -m "Update landing page"
   git push origin main
   ```
3. **GitHub Pages automatically redeploys**
   - Go to Actions tab to see deployment status
   - Site updates in 1-2 minutes

## 🌐 Your URLs

After deployment:

1. **GitHub Pages Site:**
   ```
   https://sriram07ms-collab.github.io/MutualFund-Facts-Assistant/
   ```

2. **API Endpoint** (if deployed separately):
   - Vercel: `https://your-vercel-app.vercel.app/api/query`
   - Netlify: `https://your-netlify-app.netlify.app/.netlify/functions/query`

## 🐛 Troubleshooting

### GitHub Pages Not Deploying

1. **Check GitHub Actions**
   - Go to "Actions" tab
   - Check for workflow errors
   - Review deployment logs

2. **Verify Configuration**
   - Settings → Pages → Source should be "GitHub Actions"
   - Verify `docs/index.html` exists
   - Check file is committed and pushed

3. **Check Permissions**
   - Verify GitHub Pages is enabled
   - Check workflow permissions

### API Not Working

1. **Verify API is Deployed**
   - Check Vercel/Netlify deployment
   - Verify API endpoint is accessible

2. **Update API URL**
   - Edit `docs/index.html`
   - Update API URL in selector or code
   - Commit and push changes

3. **Check CORS**
   - Verify API allows requests from GitHub Pages domain
   - Check API CORS settings

## ✅ Checklist

- [ ] GitHub Pages enabled in repository settings
- [ ] GitHub Actions workflow deployed successfully
- [ ] Landing page accessible at GitHub Pages URL
- [ ] API deployed on Vercel/Netlify (if using chat)
- [ ] API URL configured in frontend
- [ ] All links working correctly
- [ ] Mobile responsiveness tested

## 🎉 Success!

Once deployed, your GitHub Pages site will be live at:
```
https://sriram07ms-collab.github.io/MutualFund-Facts-Assistant/
```

## 📚 Additional Resources

- [GitHub Pages Documentation](https://docs.github.com/en/pages)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Vercel Deployment](VERCEL_DEPLOY.md)
- [Netlify Deployment](NETLIFY_DEPLOY.md)

## 🆘 Support

For issues:
1. Check GitHub Actions logs
2. Verify repository settings
3. Review deployment documentation
4. Check API deployment status

Happy deploying! 🚀

