#!/bin/bash

echo "🚀 Building and preparing for Vercel deployment..."

# Build the project
pip install -r requirements.txt
d2lbook build html

# Create a deployment folder
rm -rf vercel-deploy
mkdir vercel-deploy

# Copy built files to deployment folder
cp -r dist/html/* vercel-deploy/

# Copy Vercel config
cp vercel.json vercel-deploy/

echo "✅ Build complete! Deploy folder ready: vercel-deploy/"
echo ""
echo "📋 Next steps:"
echo "1. Go to vercel.com"
echo "2. Click 'New Project'"
echo "3. Choose 'Upload'"
echo "4. Drag and drop the 'vercel-deploy' folder"
echo "5. Click 'Deploy'" 