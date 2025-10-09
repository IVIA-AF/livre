#!/bin/bash

# Simple build and deploy script for local macOS M2
echo "🔨 Building MyST site locally..."
myst build --html

echo "💬 Injecting Giscus comments..."
python3 inject_giscus.py

echo "📁 Adding static files to git..."
git add _build/html/

echo "💾 Committing static files..."
git commit -m "Update static files for deployment"

echo "🚀 Pushing to GitHub..."
git push origin jupyterbook

echo "✅ Done! Vercel will automatically deploy the static files"
