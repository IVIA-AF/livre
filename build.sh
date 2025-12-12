#!/bin/bash

# Vercel build script for Jupyter Book 2 with Utterances comments
echo "🔨 Installing dependencies..."
python3 -m pip install -r requirements.txt

echo "🌎 Building Jupyter Book 2 site..."
myst build --html

# Inject Giscus comments via post-processing script
# (Plugin approach doesn't work reliably with MyST site build)
python3 inject_giscus.py

echo "✅ Build complete! Static files ready in _build/html/"
