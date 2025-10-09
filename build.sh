#!/bin/bash

# Vercel build script for MyST Jupyter Book with Giscus comments
echo "🔨 Installing MyST dependencies..."
python3 -m pip install -r requirements.txt

echo "🌎 Building MyST site..."
python3 -m myst build --html

echo "💬 Injecting Giscus comments..."
python3 inject_giscus.py

echo "✅ Build complete! Static files ready in _build/html/"
