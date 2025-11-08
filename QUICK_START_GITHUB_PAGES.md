# 🚀 Quick Start: GitHub Pages Deployment

## ✅ What's Already Done

- ✅ Code pushed to GitHub
- ✅ Landing page created (`docs/index.html`)
- ✅ GitHub Actions workflow configured (`.github/workflows/pages.yml`)
- ✅ Deployment documentation created

## 📋 Next Steps (5 Minutes)

### Step 1: Enable GitHub Pages (2 minutes)

1. **Go to Repository Settings**
   - Visit: https://github.com/sriram07ms-collab/MutualFund-Facts-Assistant/settings/pages

2. **Configure Pages**
   - Under "Source", select: **GitHub Actions**
   - Click **Save**

3. **Verify Deployment**
   - Go to **Actions** tab
   - You'll see "Deploy GitHub Pages" workflow running
   - Wait 1-2 minutes for deployment to complete

4. **Access Your Site**
   - Your landing page will be live at:
     ```
     https://sriram07ms-collab.github.io/MutualFund-Facts-Assistant/
     ```

### Step 2: Deploy Streamlit App (3 minutes)

1. **Go to Streamlit Cloud**
   - Visit: https://share.streamlit.io/
   - Sign in with your GitHub account

2. **Create New App**
   - Click **"New app"** button
   - Repository: `sriram07ms-collab/MutualFund-Facts-Assistant`
   - Branch: `main`
   - Main file path: `app.py`

3. **Add Secrets**
   - Click **"Advanced settings"**
   - Under **"Secrets"**, add:
     ```
     OPENAI_API_KEY=your_openai_api_key_here
     ```
   - Replace with your actual OpenAI API key
   - Click **"Save"**

4. **Deploy**
   - Click **"Deploy"** button
   - Wait 2-3 minutes for initial deployment
   - Note your app URL (e.g., `https://mutualfund-facts-assistant.streamlit.app`)

### Step 3: Update Landing Page Link (1 minute)

1. **Edit the HTML File**
   - Go to: https://github.com/sriram07ms-collab/MutualFund-Facts-Assistant/edit/main/docs/index.html
   - Find line with: `const streamlitUrl = 'https://mutualfund-facts-assistant.streamlit.app';`
   - Replace with your actual Streamlit Cloud URL
   - Click **"Commit changes"**

2. **Automatic Update**
   - GitHub Pages will automatically redeploy
   - Your landing page will link to the correct app

## 🎉 You're Done!

After completing these steps, you'll have:

1. **GitHub Pages Landing Page:**
   - URL: `https://sriram07ms-collab.github.io/MutualFund-Facts-Assistant/`
   - Beautiful landing page with app link

2. **Streamlit Cloud App:**
   - Your app URL (from Step 2)
   - Full RAG chatbot functionality
   - Real-time data updates

## 📊 What You Get

- ✅ Professional landing page on GitHub Pages
- ✅ Direct link to Streamlit app
- ✅ Automatic deployment on code updates
- ✅ Free hosting for both
- ✅ Mobile-responsive design
- ✅ Beautiful Groww-inspired UI

## 🔄 Automatic Updates

- **GitHub Pages**: Updates automatically when you push to `main` branch
- **Streamlit Cloud**: Updates automatically when you push to `main` branch
- **Data Refresh**: Daily automatic updates via GitHub Actions

## 🐛 Troubleshooting

### GitHub Pages Not Showing

1. Check **Actions** tab for deployment status
2. Wait 2-3 minutes after enabling Pages
3. Clear browser cache (Ctrl+Shift+R)

### Streamlit App Not Working

1. Verify `OPENAI_API_KEY` is set in Streamlit Cloud secrets
2. Check app logs in Streamlit Cloud dashboard
3. Wait for first-time data collection (5-10 minutes)

### Landing Page Link Not Working

1. Verify Streamlit app is deployed
2. Update the URL in `docs/index.html`
3. Wait for GitHub Pages to redeploy

## 📚 More Help

- Detailed guide: [GITHUB_PAGES_SETUP.md](GITHUB_PAGES_SETUP.md)
- Streamlit deployment: [STREAMLIT_CLOUD_SETUP.md](STREAMLIT_CLOUD_SETUP.md)
- General deployment: [DEPLOYMENT.md](DEPLOYMENT.md)

## ✅ Checklist

- [ ] GitHub Pages enabled in repository settings
- [ ] Landing page accessible at GitHub Pages URL
- [ ] Streamlit app deployed on Streamlit Cloud
- [ ] `OPENAI_API_KEY` added to Streamlit Cloud secrets
- [ ] Landing page link updated with Streamlit app URL
- [ ] Both sites working correctly

## 🎊 Congratulations!

Your Mutual Fund Facts Assistant is now live with:
- Professional landing page
- Full-featured chatbot app
- Automatic deployments
- Real-time data updates

Share your landing page URL with others to get started! 🚀

