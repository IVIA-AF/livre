#!/bin/bash

# Simple build and deploy script for local macOS M2
echo "🔨 Building Jupyter Book 2 site locally..."
myst build --html

# Inject Vercel Analytics
python3 inject_vercel_analytics.py

# Inject Giscus comments via post-processing script
python3 inject_giscus.py

echo "📁 Adding static files to git..."
git add _build/html/

echo "💾 Committing static files..."
git commit -m "Update static files for deployment"

echo "🚀 Pushing to GitHub..."
git push origin main

echo "✅ Done! Vercel will automatically deploy the static files"
