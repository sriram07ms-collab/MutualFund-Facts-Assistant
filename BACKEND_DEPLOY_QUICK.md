# 🚀 Quick Backend Deployment Guide

Deploy your backend API in 5 minutes using Vercel (easiest option)!

## ⚡ Quick Deploy (5 Minutes)

### Step 1: Deploy on Vercel

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
   - Click "Environment Variables"
   - Add: `OPENAI_API_KEY` = your OpenAI API key
   - Click "Save"

5. **Deploy**
   - Click "Deploy"
   - Wait 2-3 minutes
   - Your API will be live at: `https://your-project.vercel.app/api/query`

### Step 2: Update Frontend

1. **Get Your API URL**
   - After deployment, note your Vercel URL
   - API endpoint: `https://your-project.vercel.app/api/query`

2. **Update Frontend (Optional)**
   - The GitHub Pages frontend already points to the Vercel backend
   - Update `docs/index.html` only if you want to use a different API URL

### Step 3: Test

1. **Visit Your GitHub Pages Site**
   - https://sriram07ms-collab.github.io/MutualFund-Facts-Assistant/

2. **Test the Chat**
   - Ask a question
   - Verify it works!

## ✅ Done!

You now have:
- ✅ Backend API on Vercel
- ✅ Frontend on GitHub Pages
- ✅ Full-stack application working!

## 🔄 Automatic Deployment (Optional)

For automatic deployments via GitHub Actions:

1. **Get Vercel Credentials**
   - Go to Vercel Dashboard → Settings → Tokens
   - Create a new token
   - Get `ORG_ID` and `PROJECT_ID` from project settings

2. **Add GitHub Secrets** (in your existing repository)
   
   **Where to add them:**
   - Go to your GitHub repository: https://github.com/sriram07ms-collab/MutualFund-Facts-Assistant
   - Click on **Settings** (top menu bar of the repository)
   - In the left sidebar, click **Secrets and variables** → **Actions**
   - Click **New repository secret** button
   
   **Add each secret one by one:**
   - Click "New repository secret"
   - Name: `VERCEL_TOKEN` → Value: (paste your Vercel token) → Click "Add secret"
   - Click "New repository secret" again
   - Name: `VERCEL_ORG_ID` → Value: (paste your Vercel Org ID) → Click "Add secret"
   - Click "New repository secret" again
   - Name: `VERCEL_PROJECT_ID` → Value: (paste your Vercel Project ID) → Click "Add secret"
   - Click "New repository secret" again
   - Name: `OPENAI_API_KEY` → Value: (paste your OpenAI API key) → Click "Add secret"
   
   **Note:** These are NOT environment variables - they are GitHub repository secrets used by GitHub Actions workflows.

3. **Automatic Deployment**
   - The workflow will deploy on every push
   - See `.github/workflows/deploy-backend-vercel.yml`

## 🎯 Alternative: Netlify

If you prefer Netlify:

1. **Go to Netlify**
   - Visit: https://app.netlify.com/
   - Sign in with GitHub

2. **Import Project**
   - Click "Add new site" → "Import an existing project"
   - Select repository

3. **Configure**
   - Build command: (leave empty)
   - Publish directory: `public`

4. **Set Environment Variables**
   - Add: `OPENAI_API_KEY`

5. **Deploy**
   - Click "Deploy site"

## 📚 More Help

- Detailed guide: [backend-deployment-setup.md](backend-deployment-setup.md)
- Vercel docs: [VERCEL_DEPLOY.md](VERCEL_DEPLOY.md)
- Netlify docs: [NETLIFY_DEPLOY.md](NETLIFY_DEPLOY.md)

## 🆘 Troubleshooting

### API Not Working
- Check `OPENAI_API_KEY` is set correctly
- Verify API URL is correct
- Check Vercel/Netlify logs

### Frontend Can't Connect
- Verify API URL in frontend
- Check CORS settings
- Test API endpoint directly

Happy deploying! 🚀

