#!/bin/bash
# Setup script for GitHub repository

echo "Setting up GitHub repository..."

# Initialize git if not already done
if [ ! -d .git ]; then
    echo "Initializing git repository..."
    git init
    git branch -M main
fi

# Add remote if not exists (using HTTPS for easier authentication)
if ! git remote | grep -q origin; then
    echo "Adding remote repository (HTTPS)..."
    git remote add origin https://github.com/fahimehorvatinia/Group20-Data-Mining-Project.git
else
    # Update to HTTPS if it's using SSH
    current_url=$(git remote get-url origin)
    if [[ $current_url == git@* ]]; then
        echo "Switching remote to HTTPS..."
        git remote set-url origin https://github.com/fahimehorvatinia/Group20-Data-Mining-Project.git
    fi
fi

# Add files
echo "Adding files to git..."
git add .gitignore
git add README.md
git add ESC_50_Complete_Project_All_Methods.ipynb
git add extract_results.py
git add results.html
git add data_out/*.csv
git add ESC-50_data/meta/
git add ESC-50_data/README.md
git add ESC-50_data/LICENSE
git add GITHUB_SETUP.md
git add GITHUB_AUTH.md
git add QUICK_START.md
git add push_to_github.sh

# Commit
echo "Committing files..."
git commit -m "Initial commit: ESC-50 Sound Classification Project

- Complete project notebook with all models
- Results visualization website
- Feature extraction files
- Documentation and setup scripts
- Note: Report files excluded (see .gitignore)"

echo ""
echo "Setup complete!"
echo ""
echo "To push to GitHub, run:"
echo "   ./push_to_github.sh"
echo "   (or: git push -u origin main)"
echo ""
echo "Note: Large files (audio data, zip files) are excluded via .gitignore"
echo ""
echo "Authentication:"
echo "   You'll need a Personal Access Token (not your password)"
echo "   Create one at: https://github.com/settings/tokens"
echo "   See GITHUB_AUTH.md for details"

