#!/bin/bash

# Development server script that builds and injects comments
echo "🔨 Building MyST site..."
myst build --html

echo "💬 Injecting Giscus comments..."
python3 inject_giscus.py

echo "🚀 Starting development server..."
echo "📍 The site is now available at: http://localhost:3002"
echo "💡 Note: Comments are injected into static files, not the dev server"
echo "   For testing comments, use: python3 -m http.server 8080 -d _build/html"

# Start the development server
myst start
