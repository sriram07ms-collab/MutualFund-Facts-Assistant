# GitHub Pages Quick Start ✅

Deploy the frontend and connect it to the live Vercel backend in three steps.

## 1. Enable GitHub Pages

1. Open repository settings → **Pages**
2. Set **Source** to **GitHub Actions**
3. Save and watch the **Deploy GitHub Pages** workflow in the **Actions** tab

Your site is published at:
```
https://sriram07ms-collab.github.io/MutualFund-Facts-Assistant/
```

## 2. Backend API

The frontend already targets the shared Vercel deployment:
```
https://mutual-fund-facts-assistant.vercel.app/api/query
```

If you deploy your own backend, edit `docs/index.html` and update:
```javascript
const API_URL = 'https://your-backend.vercel.app/api/query';
```

## 3. Test the Chat

Open the GitHub Pages URL, ask a question, and verify you receive a response with citations.

## Optional Enhancements

- Customize copy or styling in `docs/index.html`
- Deploy your own backend via Vercel/Netlify (see `backend-deployment-setup.md`)

## Troubleshooting

- **Pages workflow failed?** Check the run log in the Actions tab
- **API error?** Confirm your backend is responding and the `API_URL` is correct
- **Stale page?** Hard refresh or clear cache

Done! 🚀

