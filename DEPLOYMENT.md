# Deployment Guide

This guide covers the recommended deployment paths for the Mutual Fund Facts Assistant.

## 1. GitHub Pages + Vercel (Recommended)

- **Frontend**: GitHub Pages hosts `docs/index.html`
- **Backend**: Vercel hosts the serverless API (`api/query.py`)

### Steps
1. Enable GitHub Pages (Settings → Pages → Source: GitHub Actions)
2. Import the repository into Vercel and set `OPENAI_API_KEY`
3. Deploy – the default Vercel deployment URL is embedded in the frontend
4. (Optional) Update `API_URL` in `docs/index.html` with your own Vercel URL

See [VERCEL_DEPLOY.md](VERCEL_DEPLOY.md) and [GITHUB_PAGES_DEPLOY.md](GITHUB_PAGES_DEPLOY.md) for details.

## 2. GitHub Pages + Netlify

- Same approach as above, but the backend API lives on Netlify
- Update `API_URL` with the Netlify function endpoint `/.netlify/functions/query`

See [NETLIFY_DEPLOY.md](NETLIFY_DEPLOY.md) for details.

## 3. Railway / Render

These platforms can host the Python API if you prefer a containerized deployment.  
Use the provided scripts to collect data and build the vector store during build/startup.

## Environment Variables

Set at least:
```
OPENAI_API_KEY=your_openai_api_key_here
```

Optional overrides live in `config.py`.

## Automated Data Refresh

`.github/workflows/data-refresh.yml` runs daily:
- Collects data
- Rebuilds the vector store
- Commits any updates

Add `OPENAI_API_KEY` as a repository secret to enable the workflow.

## Updating the Frontend

1. Modify `docs/index.html`
2. Commit and push
3. GitHub Pages redeploys automatically

## Troubleshooting

- **Pages build fails**: check the Actions log
- **API errors**: verify your backend deployment and environment variables
- **First request slow**: data collection & vector store build happen on demand; subsequent calls are fast

Happy shipping! 🚀

