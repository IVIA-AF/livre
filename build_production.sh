#!/bin/bash

# Production build script for deployment
echo "🔨 Building Jupyter Book 2 site for production..."
myst build --html

# Inject Vercel Analytics
python3 inject_vercel_analytics.py

# Inject Giscus comments via post-processing script
python3 inject_giscus.py

echo "✅ Production build complete!"
echo "📍 Static files are ready in: _build/html/"
echo "🚀 Deploy the _build/html/ directory to any static hosting service"
echo ""
echo "📋 Files ready for deployment:"
ls -la _build/html/
