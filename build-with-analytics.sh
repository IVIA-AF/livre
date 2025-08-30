#!/bin/bash

echo "🚀 Building IVIA-AF Book with Analytics and Comments..."

# Build the project
echo "📦 Building with d2l-book..."
d2lbook build html

# Copy analytics.js to _static directory
echo "📊 Copying analytics.js to _static directory..."
cp static/analytics.js dist/html/_static/analytics.js

# Add analytics scripts to all HTML files
echo "📊 Adding analytics scripts to HTML files..."
find dist/html -name "*.html" -exec sed -i '' 's|<script type="text/javascript" src="_static/sphinx_materialdesign_theme.js "></script>|<script type="text/javascript" src="_static/sphinx_materialdesign_theme.js "></script>\
    <!-- Vercel Analytics -->\
    <script defer src="https://va.vercel-scripts.com/v1/script.js"></script>\
    <script src="_static/analytics.js"></script>|' {} \;

# Inject Disqus comments into HTML files
echo "💬 Injecting Disqus comments into HTML files..."
python3 inject_comments.py

echo "✅ Build complete with analytics and comments!"
echo ""
echo "📋 Next steps:"
echo "1. Update DISQUS_SHORTNAME in inject_comments.py with your actual shortname"
echo "2. git add dist/html/"
echo "3. git commit -m 'Update built files with analytics and comments'"
echo "4. git push origin vercel-static" 