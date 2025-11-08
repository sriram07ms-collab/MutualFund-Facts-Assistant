# GitHub Pages Deployment Guide

This guide explains how to publish the Mutual Fund Facts Assistant frontend on GitHub Pages and connect it to the backend API hosted on Vercel (or any other platform you choose).

## 📋 Prerequisites

- GitHub repository: `sriram07ms-collab/MutualFund-Facts-Assistant`
- Backend API deployed (default: Vercel deployment included with this project)

## 🚀 Step-by-Step Setup

### 1. Enable GitHub Pages

1. Open repository settings:  
   https://github.com/sriram07ms-collab/MutualFund-Facts-Assistant/settings
2. Scroll to **Pages**
3. Under **Source**, choose **GitHub Actions**
4. Click **Save**

The workflow in `.github/workflows/pages.yml` will run automatically. Monitor it in the **Actions** tab. When the run succeeds, your site is live at:

```
https://sriram07ms-collab.github.io/MutualFund-Facts-Assistant/
```

### 2. (Optional) Use a Custom API Endpoint

The frontend defaults to the shared Vercel backend (`https://mutual-fund-facts-assistant.vercel.app/api/query`). To point to a different backend:

1. Edit `docs/index.html`
2. Update the line:
   ```javascript
   const API_URL = 'https://mutual-fund-facts-assistant.vercel.app/api/query';
   ```
3. Commit and push the change  
   GitHub Pages will redeploy automatically.

## 🔄 Automatic Updates

- Every push to `main` triggers the Pages workflow
- The site is rebuilt and redeployed automatically
- No manual steps required after you push changes

## 🧩 Customizing the Frontend

- Modify copy, styling, or layout in `docs/index.html`
- Add new sections (FAQs, contact, etc.) directly in the HTML
- CSS lives inside the `<style>` block at the top of the file

## ✅ Checklist

- [ ] GitHub Pages enabled in repository settings  
- [ ] Pages workflow succeeded  
- [ ] Frontend loads at the GitHub Pages URL  
- [ ] Backend API reachable (default Vercel endpoint)  
- [ ] `API_URL` updated if you use your own backend  

## 🐛 Troubleshooting

- **Pages build failing?** Check the run logs in the **Actions** tab  
- **Site not updating?** Make sure you committed your changes and the workflow re-ran  
- **API error in UI?** Verify your backend deployment and the `API_URL` value  

## 📚 Related Docs

- [backend-deployment-setup.md](backend-deployment-setup.md) – deploying the API  
- [VERCEL_DEPLOY.md](VERCEL_DEPLOY.md) – detailed Vercel steps  
- [NETLIFY_DEPLOY.md](NETLIFY_DEPLOY.md) – Netlify option  
- [DEPLOYMENT_SUMMARY.md](DEPLOYMENT_SUMMARY.md) – overall view

Happy deploying! 🚀

