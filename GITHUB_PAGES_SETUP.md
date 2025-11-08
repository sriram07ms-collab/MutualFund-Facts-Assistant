# GitHub Pages Deployment Guide

This guide explains how to deploy the Mutual Fund Facts Assistant landing page using GitHub Pages and link it to your Streamlit Cloud app.

## 🎯 Overview

GitHub Pages will host a beautiful landing page that links to your Streamlit Cloud application. This provides:
- ✅ Professional landing page
- ✅ Easy sharing with a clean URL
- ✅ Documentation and links to the app
- ✅ Free hosting on GitHub Pages

## 📋 Prerequisites

- GitHub repository: `sriram07ms-collab/MutualFund-Facts-Assistant`
- Code pushed to GitHub (✅ Already done)

## 🚀 Step-by-Step Setup

### Step 1: Enable GitHub Pages

1. **Go to Repository Settings**
   - Navigate to: https://github.com/sriram07ms-collab/MutualFund-Facts-Assistant/settings
   - Scroll down to "Pages" section

2. **Configure GitHub Pages**
   - Under "Source", select: **GitHub Actions**
   - Click "Save"

3. **Verify Deployment**
   - The GitHub Actions workflow (`.github/workflows/pages.yml`) will automatically deploy
   - Go to "Actions" tab to see the deployment status
   - Once deployed, your site will be available at:
     ```
     https://sriram07ms-collab.github.io/MutualFund-Facts-Assistant/
     ```

### Step 2: Deploy Streamlit App (If Not Done)

1. **Go to Streamlit Cloud**
   - Visit: https://share.streamlit.io/
   - Sign in with GitHub

2. **Deploy App**
   - Click "New app"
   - Select repository: `sriram07ms-collab/MutualFund-Facts-Assistant`
   - Branch: `main`
   - Main file: `app.py`
   - Add `OPENAI_API_KEY` in secrets
   - Click "Deploy"

3. **Get Streamlit App URL**
   - After deployment, note your Streamlit app URL
   - Example: `https://mutualfund-facts-assistant.streamlit.app`

### Step 3: Update Landing Page Link

1. **Update the App Link**
   - Edit `docs/index.html`
   - Find the line with `streamlitUrl`
   - Update with your actual Streamlit Cloud URL:
     ```javascript
     const streamlitUrl = 'https://your-app-name.streamlit.app';
     ```

2. **Commit and Push**
   ```bash
   git add docs/index.html
   git commit -m "Update Streamlit app URL"
   git push origin main
   ```

3. **GitHub Pages will auto-update**
   - The workflow will automatically redeploy
   - Your landing page will link to the correct app

## 🔄 Automatic Deployment

The GitHub Actions workflow (`.github/workflows/pages.yml`) automatically:
- Deploys on every push to `main` branch
- Updates the landing page
- Makes it available on GitHub Pages

## 🌐 Your URLs

After setup, you'll have:

1. **GitHub Pages Landing Page:**
   ```
   https://sriram07ms-collab.github.io/MutualFund-Facts-Assistant/
   ```

2. **Streamlit Cloud App:**
   ```
   https://your-app-name.streamlit.app
   ```

3. **GitHub Repository:**
   ```
   https://github.com/sriram07ms-collab/MutualFund-Facts-Assistant
   ```

## 🎨 Customization

### Update Landing Page Content

Edit `docs/index.html` to customize:
- Header text and description
- Features list
- Example questions
- Colors and styling
- Links and resources

### Change Theme Colors

In `docs/index.html`, update the CSS variables:
```css
background: linear-gradient(135deg, #00D09C 0%, #00B887 100%);
```

### Add More Sections

Add new sections to the landing page by editing `docs/index.html`:
- About section
- Features grid
- FAQ section
- Contact information

## 🔍 Verification

1. **Check GitHub Pages Status**
   - Go to: Settings → Pages
   - Verify "GitHub Actions" is selected
   - Check deployment status

2. **Test Landing Page**
   - Visit: https://sriram07ms-collab.github.io/MutualFund-Facts-Assistant/
   - Verify all links work
   - Check mobile responsiveness

3. **Test Streamlit App Link**
   - Click "Launch App" button
   - Verify it opens the Streamlit app
   - Test app functionality

## 🐛 Troubleshooting

### GitHub Pages Not Deploying

1. **Check GitHub Actions**
   - Go to "Actions" tab
   - Check for workflow errors
   - Review deployment logs

2. **Verify File Structure**
   - Ensure `docs/index.html` exists
   - Check file is committed and pushed

3. **Check Permissions**
   - Verify GitHub Pages is enabled
   - Check workflow permissions

### Landing Page Not Updating

1. **Clear Browser Cache**
   - Hard refresh: Ctrl+Shift+R (Windows) or Cmd+Shift+R (Mac)

2. **Check Deployment Status**
   - Go to Actions tab
   - Verify latest deployment succeeded

3. **Wait for Propagation**
   - GitHub Pages updates can take a few minutes

### Streamlit App Link Not Working

1. **Verify Streamlit App URL**
   - Check Streamlit Cloud dashboard
   - Verify app is deployed and running

2. **Update HTML File**
   - Edit `docs/index.html`
   - Update the `streamlitUrl` variable
   - Commit and push changes

## 📊 Monitoring

- **GitHub Pages**: Check deployment status in Actions tab
- **Streamlit Cloud**: Monitor app usage in Streamlit Cloud dashboard
- **GitHub Actions**: Review workflow runs for any issues

## 🔄 Updates

To update the landing page:

1. Edit `docs/index.html`
2. Commit changes:
   ```bash
   git add docs/index.html
   git commit -m "Update landing page"
   git push origin main
   ```
3. GitHub Pages will automatically redeploy

## ✅ Checklist

- [ ] GitHub Pages enabled in repository settings
- [ ] GitHub Actions workflow deployed successfully
- [ ] Landing page accessible at GitHub Pages URL
- [ ] Streamlit app deployed on Streamlit Cloud
- [ ] App link updated in landing page
- [ ] All links working correctly
- [ ] Mobile responsiveness tested

## 🎉 Success!

Once set up, you'll have:
- ✅ Professional landing page on GitHub Pages
- ✅ Direct link to Streamlit app
- ✅ Automatic deployment on code updates
- ✅ Free hosting for both

Your Mutual Fund Facts Assistant is now live with a beautiful landing page! 🚀

## 📚 Additional Resources

- [GitHub Pages Documentation](https://docs.github.com/en/pages)
- [Streamlit Cloud Documentation](https://docs.streamlit.io/streamlit-community-cloud)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)

## 🆘 Support

If you encounter issues:
1. Check GitHub Actions logs
2. Verify repository settings
3. Review deployment documentation
4. Check Streamlit Cloud status

For more help, see:
- [DEPLOYMENT.md](DEPLOYMENT.md)
- [STREAMLIT_CLOUD_SETUP.md](STREAMLIT_CLOUD_SETUP.md)
- [README.md](README.md)

