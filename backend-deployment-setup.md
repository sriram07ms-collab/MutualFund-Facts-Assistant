# Backend Deployment Setup Guide

This guide explains how to deploy the backend API on various platforms using GitHub Actions.

## 🎯 Options for Backend Deployment

Since GitHub Pages only supports static files, you need to deploy the backend API to a platform that supports serverless functions or Python applications.

### Option 1: Vercel (Recommended - Easiest)

**Automatic Deployment via GitHub Actions**

1. **Get Vercel Credentials**
   - Go to [Vercel Dashboard](https://vercel.com/dashboard)
   - Go to Settings → Tokens
   - Create a new token
   - Go to your project settings to get `ORG_ID` and `PROJECT_ID`

2. **Add GitHub Secrets**
   - Go to: https://github.com/sriram07ms-collab/MutualFund-Facts-Assistant/settings/secrets/actions
   - Add the following secrets:
     - `VERCEL_TOKEN` - Your Vercel token
     - `VERCEL_ORG_ID` - Your Vercel organization ID
     - `VERCEL_PROJECT_ID` - Your Vercel project ID
     - `OPENAI_API_KEY` - Your OpenAI API key

3. **Deploy via GitHub Actions**
   - The workflow (`.github/workflows/deploy-backend-vercel.yml`) will automatically deploy on push
   - Or manually trigger it from the Actions tab

4. **Get API URL**
   - After deployment, get your Vercel deployment URL
   - API endpoint: `https://your-project.vercel.app/api/query`

### Option 2: Netlify

**Automatic Deployment via GitHub Actions**

1. **Get Netlify Credentials**
   - Go to [Netlify Dashboard](https://app.netlify.com/)
   - Go to User settings → Applications → New access token
   - Create a new token
   - Create a new site or use an existing one
   - Get your `SITE_ID` from site settings

2. **Add GitHub Secrets**
   - Go to: https://github.com/sriram07ms-collab/MutualFund-Facts-Assistant/settings/secrets/actions
   - Add the following secrets:
     - `NETLIFY_AUTH_TOKEN` - Your Netlify token
     - `NETLIFY_SITE_ID` - Your Netlify site ID
     - `OPENAI_API_KEY` - Your OpenAI API key

3. **Deploy via GitHub Actions**
   - The workflow (`.github/workflows/deploy-backend-netlify.yml`) will automatically deploy on push
   - Or manually trigger it from the Actions tab

4. **Get API URL**
   - After deployment, get your Netlify deployment URL
   - API endpoint: `https://your-site.netlify.app/.netlify/functions/query`

### Option 3: Manual Vercel Deployment (Simpler)

**Deploy directly from Vercel Dashboard**

1. **Go to Vercel**
   - Visit: https://vercel.com/
   - Sign in with GitHub

2. **Import Project**
   - Click "Add New Project"
   - Select repository: `sriram07ms-collab/MutualFund-Facts-Assistant`
   - Click "Import"

3. **Configure Project**
   - Framework Preset: **Other**
   - Root Directory: `./`
   - Build Command: (leave empty)
   - Output Directory: `public`

4. **Set Environment Variables**
   - Add: `OPENAI_API_KEY` = your OpenAI API key
   - Click "Deploy"

5. **Get API URL**
   - After deployment, note your Vercel URL
   - API endpoint: `https://your-project.vercel.app/api/query`

### Option 4: Manual Netlify Deployment

**Deploy directly from Netlify Dashboard**

1. **Go to Netlify**
   - Visit: https://app.netlify.com/
   - Sign in with GitHub

2. **Add New Site**
   - Click "Add new site" → "Import an existing project"
   - Select "GitHub"
   - Select repository: `sriram07ms-collab/MutualFund-Facts-Assistant`

3. **Configure Build Settings**
   - Build command: (leave empty)
   - Publish directory: `public`

4. **Set Environment Variables**
   - Add: `OPENAI_API_KEY` = your OpenAI API key
   - Click "Deploy site"

5. **Get API URL**
   - After deployment, note your Netlify URL
   - API endpoint: `https://your-site.netlify.app/.netlify/functions/query`

## 🔗 Connecting Frontend to Backend

After deploying the backend, update the frontend to use the API URL:

### Option 1: Update docs/index.html

Edit `docs/index.html` and update the API URL selector:

```javascript
// Add your deployed API URL
const API_URL = 'https://your-vercel-app.vercel.app/api/query';
// or
const API_URL = 'https://your-netlify-app.netlify.app/.netlify/functions/query';
```

### Option 2: Use Environment Variable (For Vercel/Netlify Frontend)

If you deploy the frontend on Vercel/Netlify as well, you can use environment variables:

```javascript
const API_URL = process.env.API_URL || '/api/query';
```

## 📋 GitHub Actions Workflows

The repository includes workflows for automatic deployment:

1. **deploy-backend-vercel.yml** - Deploys to Vercel
2. **deploy-backend-netlify.yml** - Deploys to Netlify
3. **deploy-backend-railway.yml** - Deploys to Railway (optional)

## 🔄 Automatic Deployment

Once configured, the workflows will automatically:
- Deploy backend on every push to `main` branch
- Deploy when backend files change
- Update deployment URLs

## ✅ Checklist

- [ ] Choose deployment platform (Vercel/Netlify)
- [ ] Get platform credentials
- [ ] Add secrets to GitHub
- [ ] Deploy backend (manual or automatic)
- [ ] Get API URL
- [ ] Update frontend with API URL
- [ ] Test API endpoint
- [ ] Verify frontend-backend connection

## 🎉 Success!

Once deployed, you'll have:
- ✅ Backend API deployed on Vercel/Netlify
- ✅ Frontend on GitHub Pages
- ✅ Full-stack application working
- ✅ Automatic deployments on code changes

## 🆘 Troubleshooting

### Backend Not Deploying

1. **Check GitHub Secrets**
   - Verify all required secrets are set
   - Check secret names match workflow requirements

2. **Check Workflow Logs**
   - Go to Actions tab
   - Check workflow logs for errors
   - Verify credentials are correct

### API Not Working

1. **Verify API URL**
   - Check deployment URL is correct
   - Verify API endpoint path is correct

2. **Check Environment Variables**
   - Verify `OPENAI_API_KEY` is set
   - Check API logs for errors

3. **Test API Endpoint**
   - Use curl or Postman to test
   - Check response for errors

## 📚 Resources

- [Vercel Documentation](https://vercel.com/docs)
- [Netlify Documentation](https://docs.netlify.com/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)

Happy deploying! 🚀

