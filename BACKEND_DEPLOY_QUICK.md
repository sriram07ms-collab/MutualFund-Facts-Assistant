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
   - The frontend already has a default Vercel URL
   - Or update `docs/index.html` with your specific URL
   - The API selector in the frontend will let you choose the endpoint

### Step 3: Test

1. **Visit Your GitHub Pages Site**
   - https://sriram07ms-collab.github.io/MutualFund-Facts-Assistant/

2. **Select API Endpoint**
   - Use the dropdown to select your Vercel deployment
   - Or it will use the default

3. **Test the Chat**
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

2. **Add GitHub Secrets**
   - Go to: https://github.com/sriram07ms-collab/MutualFund-Facts-Assistant/settings/secrets/actions
   - Add:
     - `VERCEL_TOKEN`
     - `VERCEL_ORG_ID`
     - `VERCEL_PROJECT_ID`
     - `OPENAI_API_KEY`

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

