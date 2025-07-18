#!/bin/bash

echo "🚀 Building IVIA-AF Book with Analytics..."

# Build the project
echo "📦 Building with d2l-book..."
d2lbook build html

# Add analytics scripts to all HTML files
echo "📊 Adding analytics scripts to HTML files..."
find dist/html -name "*.html" -exec sed -i '' 's|<script type="text/javascript" src="_static/sphinx_materialdesign_theme.js "></script>|<script type="text/javascript" src="_static/sphinx_materialdesign_theme.js "></script>\
    <!-- Vercel Analytics -->\
    <script defer src="https://va.vercel-scripts.com/v1/script.js"></script>\
    <script src="_static/analytics.js"></script>|' {} \;

echo "✅ Build complete with analytics!"
echo ""
echo "📋 Next steps:"
echo "1. git add dist/html/"
echo "2. git commit -m 'Update built files with analytics'"
echo "3. git push origin vercel-static" 