# GitHub Repository Setup Guide

## Quick Start

### 1. Initialize and Push to GitHub

```bash
# Run the setup script
./setup_git.sh

# Push to GitHub
git push -u origin main
```

### 2. Update Results Website

After running your notebook and getting actual results:

1. **Option A: Manual Update**
   - Open `results.html`
   - Find the `modelResults` array (around line 280)
   - Update with your actual test accuracies

2. **Option B: Extract from Notebook** (if you have results in outputs)
   ```bash
   python3 extract_results.py
   ```

## Files Included in Repository

**Included:**
- `ESC_50_Complete_Project_All_Methods.ipynb` - Main notebook
- `Project_Report.tex` - Report source
- `results.html` - Results website
- `README.md` - Project documentation
- `data_out/*.csv` - Feature files (small, ~7MB each)
- `ESC-50_data/meta/` - Metadata only
- Documentation files

**Excluded (via .gitignore):**
- `ESC-50_data/audio/` - Audio files (844MB)
- `ESC-50.zip` - Dataset zip (616MB)
- `*.npy` - Embedding cache files
- `*.pkl` - Large model files
- `__pycache__/` - Python cache
- `.ipynb_checkpoints/` - Jupyter checkpoints

## GitHub Pages Setup (Optional)

To host the results website on GitHub Pages:

1. Go to repository Settings → Pages
2. Select source: `main` branch
3. Select folder: `/ (root)`
4. Save
5. Your website will be available at:
   `https://fahimehorvatinia.github.io/Group20-Data-Mining-Project/results.html`

## Updating Results

### Step 1: Run Your Notebook
Complete all model training and evaluation in the notebook.

### Step 2: Extract Results
Look for the results dataframes in your notebook outputs. They should show:
- Model name
- Dataset type (Raw/Normalized/Selected)
- Test accuracy

### Step 3: Update results.html
Edit the JavaScript array in `results.html`:

```javascript
const modelResults = [
    {"name": "Logistic Regression", "member": "Sushama", "raw": 0.45, "norm": 0.52, "sel": 0.48},
    {"name": "KNN", "member": "Sushama", "raw": 0.38, "norm": 0.41, "sel": 0.39},
    // ... update with your actual results
];
```

### Step 4: Commit and Push
```bash
git add results.html
git commit -m "Update results with actual model performance"
git push
```

## Results Website Features

The `results.html` website includes:
- Beautiful, responsive design
- Interactive comparison table
- Bar chart visualization (Chart.js)
- Team member contributions
- Key findings section
- Mobile-friendly layout

## Important Notes

1. **Large Files**: Audio data and zip files are excluded to save GitHub space
2. **Feature CSVs**: Included because they're needed to run the notebook (only ~7MB each)
3. **Privacy**: Make sure no sensitive data is in the repository
4. **License**: The ESC-50 dataset has its own license - included in `ESC-50_data/LICENSE`

## Repository Structure

```
Group20-Data-Mining-Project/
├── .gitignore              # Excludes large files
├── README.md               # Project documentation
├── results.html            # Results website
├── ESC_50_Complete_Project_All_Methods.ipynb
├── Project_Report.tex
├── extract_results.py      # Helper script
├── setup_git.sh           # Setup script
├── data_out/              # Feature files (CSV)
│   ├── esc50_features_raw.csv
│   ├── esc50_features_normalized_corrected.csv
│   └── esc50_features_selected.csv
└── ESC-50_data/           # Dataset metadata only
    ├── meta/
    ├── README.md
    └── LICENSE
```

## Troubleshooting

### Issue: "Repository not found"
- Check that you've created the repository on GitHub first
- Verify the remote URL: `git remote -v`

### Issue: "Large file rejected"
- Check `.gitignore` is working: `git status`
- If a large file was added, remove it: `git rm --cached <file>`

### Issue: Results not showing
- Open browser console (F12) to check for JavaScript errors
- Verify Chart.js CDN is loading
- Check that modelResults array is valid JSON

## Checklist Before Pushing

- [ ] All large files excluded (check `.gitignore`)
- [ ] Results updated in `results.html`
- [ ] README.md is complete
- [ ] No sensitive data in repository
- [ ] Notebook runs without errors
- [ ] All team members listed correctly

## Need Help?

If you encounter issues:
1. Check GitHub documentation
2. Verify file sizes: `du -sh *`
3. Check git status: `git status`
4. Review `.gitignore` file

