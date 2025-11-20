#!/bin/bash
# Push to GitHub using HTTPS (easier than SSH)

echo "Pushing to GitHub..."

# Check if remote is set
if ! git remote | grep -q origin; then
    echo "Setting up remote..."
    git remote add origin https://github.com/fahimehorvatinia/Group20-Data-Mining-Project.git
fi

# Ensure we're using HTTPS
current_url=$(git remote get-url origin)
if [[ $current_url == git@* ]]; then
    echo "Switching from SSH to HTTPS..."
    git remote set-url origin https://github.com/fahimehorvatinia/Group20-Data-Mining-Project.git
fi

echo "Pushing to GitHub..."
echo ""
echo "You may be prompted for your GitHub username and password"
echo "For password, use a Personal Access Token (not your GitHub password)"
echo "Create one at: https://github.com/settings/tokens"
echo ""

git push -u origin main

if [ $? -eq 0 ]; then
    echo ""
    echo "Successfully pushed to GitHub!"
    echo "View your repository at:"
    echo "   https://github.com/fahimehorvatinia/Group20-Data-Mining-Project"
else
    echo ""
    echo "Push failed. Common issues:"
    echo "   1. Repository doesn't exist on GitHub - create it first"
    echo "   2. Need to authenticate - use Personal Access Token"
    echo "   3. No commits yet - run: git add . && git commit -m 'Initial commit'"
fi

