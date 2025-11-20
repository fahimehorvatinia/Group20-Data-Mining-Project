#!/bin/bash
# Check GitHub Pages setup

echo "=========================================="
echo "GitHub Pages Setup Check"
echo "=========================================="
echo ""

# Check if results.html exists
if [ -f "results.html" ]; then
    echo "[OK] results.html exists"
else
    echo "[ERROR] results.html not found"
    exit 1
fi

# Check if index.html exists
if [ -f "index.html" ]; then
    echo "[OK] index.html exists"
else
    echo "[WARN] index.html not found (optional)"
fi

# Check git status
echo ""
echo "Git Status:"
echo "-----------"
git status --short | head -10

# Check remote
echo ""
echo "Remote Repository:"
echo "------------------"
git remote -v

# Check branch
echo ""
echo "Current Branch:"
echo "---------------"
git branch --show-current

# Check recent commits
echo ""
echo "Recent Commits:"
echo "---------------"
git log --oneline -3

echo ""
echo "=========================================="
echo "Next Steps:"
echo "=========================================="
echo ""
echo "1. If files need to be pushed:"
echo "   git add ."
echo "   git commit -m 'Add website files'"
echo "   git push"
echo ""
echo "2. Enable GitHub Pages:"
echo "   - Go to: https://github.com/fahimehorvatinia/Group20-Data-Mining-Project/settings/pages"
echo "   - Select 'main' branch"
echo "   - Select '/ (root)' folder"
echo "   - Click Save"
echo ""
echo "3. Wait 1-2 minutes, then visit:"
echo "   https://fahimehorvatinia.github.io/Group20-Data-Mining-Project/"
echo "   or"
echo "   https://fahimehorvatinia.github.io/Group20-Data-Mining-Project/results.html"
echo ""

