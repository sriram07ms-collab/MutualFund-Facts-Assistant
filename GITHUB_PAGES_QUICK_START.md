# 🚀 GitHub Pages Quick Start

Deploy the frontend in minutes and connect it to the live backend.

## 1. Enable GitHub Pages

1. Go to repository **Settings → Pages**
2. Choose **Source: GitHub Actions**
3. Save and watch the **Deploy GitHub Pages** workflow complete

Your site appears at:
```
https://sriram07ms-collab.github.io/MutualFund-Facts-Assistant/
```

## 2. Backend API (Already Live)

The frontend calls the production API at:
```
https://mutual-fund-facts-assistant.vercel.app/api/query
```

If you deploy your own backend (Vercel/Netlify), update the line in `docs/index.html`:
```javascript
const API_URL = 'https://your-backend.example.com/api/query';
```
Commit and push to trigger a new Pages deployment.

## 3. Test the Chat

Open the GitHub Pages URL, ask a question, and confirm the response includes the source citation.

## Optional Enhancements

- Customize copy and styling in `docs/index.html`
- Deploy a personal backend following `backend-deployment-setup.md`

## Troubleshooting

- **Pages workflow failed?** Inspect the log in the Actions tab
- **API error?** Ensure the backend endpoint is reachable
- **Stale content?** Force refresh or clear browser cache

You’re live! 🎉

