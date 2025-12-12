#!/bin/bash

# Development server script for Jupyter Book 2
echo "🔨 Building Jupyter Book 2 site..."
myst build --html

# Inject Giscus comments via post-processing script
python3 inject_giscus.py

echo "🚀 Starting local server with CSP headers for Giscus..."
python3 serve_local.py
