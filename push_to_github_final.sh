#!/bin/bash
# Final push script - excludes report files

echo "Preparing to push to GitHub (report files excluded)..."

# Check if .gitignore excludes report files
if ! grep -q "Project_Report.tex" .gitignore; then
    echo "Warning: Report files not in .gitignore"
fi

# Remove report files from git if they were tracked
git rm --cached Project_Report.tex Report_Figures_Guide.md Report_Summary.md 2>/dev/null

# Add all non-ignored files
echo "Adding files to git..."
git add .

# Check what will be committed
echo ""
echo "Files to be committed:"
git status --short

echo ""
echo "Pushing to GitHub..."
echo "You may be prompted for your GitHub username and Personal Access Token"
echo ""

git push -u origin main

if [ $? -eq 0 ]; then
    echo ""
    echo "Successfully pushed to GitHub!"
    echo ""
    echo "Next steps:"
    echo "1. Enable GitHub Pages:"
    echo "   - Go to: https://github.com/fahimehorvatinia/Group20-Data-Mining-Project/settings/pages"
    echo "   - Select 'main' branch and '/ (root)' folder"
    echo "   - Click Save"
    echo ""
    echo "2. Your website will be available at:"
    echo "   https://fahimehorvatinia.github.io/Group20-Data-Mining-Project/results.html"
    echo ""
    echo "3. See WEBSITE_SETUP.md for detailed instructions"
else
    echo ""
    echo "Push failed. Check the error message above."
fi

