#!/bin/bash

echo "🚀 Building IVIA-AF Book with Analytics and Giscus Comments..."

# Build the project
echo "📦 Building with d2l-book..."
d2lbook build html

# Copy analytics.js to _static directory
echo "📊 Copying analytics.js to _static directory..."
cp static/analytics.js dist/html/_static/analytics.js

# Copy custom template to _templates directory
echo "📄 Copying custom template to _templates directory..."
mkdir -p dist/html/_templates
cp static/custom_template.html dist/html/_templates/

# Add analytics scripts to all HTML files
echo "📊 Adding analytics scripts to HTML files..."
find dist/html -name "*.html" -exec sed -i '' 's|<script type="text/javascript" src="_static/sphinx_materialdesign_theme.js "></script>|<script type="text/javascript" src="_static/sphinx_materialdesign_theme.js "></script>\
    <!-- Vercel Analytics -->\
    <script defer src="https://va.vercel-scripts.com/v1/script.js"></script>\
    <script src="_static/analytics.js"></script>|' {} \;

# Inject Giscus comments using Python script (more reliable than sed)
echo "💬 Injecting Giscus comments using Python script..."
python inject-giscus.py

echo "✅ Build complete with analytics and Giscus comments!"
echo ""
echo "📋 Next steps:"
echo "1. Test locally: npm run serve-csp"
echo "2. Open http://localhost:8000 in your browser"
echo "3. Check if comments appear with proper styling and visibility"
echo "4. If everything works, commit and push your changes"
echo ""
echo "🔧 To test locally:"
echo "   npm run serve-csp"
echo "   Then open http://localhost:8000 in your browser" 