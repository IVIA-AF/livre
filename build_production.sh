#!/bin/bash

# Production build script for deployment
echo "🔨 Building MyST site for production..."
myst build --html

echo "💬 Injecting Giscus comments..."
python3 inject_giscus.py

echo "✅ Production build complete!"
echo "📍 Static files are ready in: _build/html/"
echo "🚀 Deploy the _build/html/ directory to any static hosting service"
echo ""
echo "📋 Files ready for deployment:"
ls -la _build/html/
