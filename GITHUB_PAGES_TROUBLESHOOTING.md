# GitHub Pages 404 Error - Troubleshooting Guide

## Common Causes and Solutions

### Issue 1: GitHub Pages Not Enabled

**Solution:**
1. Go to your repository: `https://github.com/fahimehorvatinia/Group20-Data-Mining-Project`
2. Click **Settings** (top right)
3. Scroll to **Pages** in the left sidebar
4. Under **Source**, select:
   - Branch: `main`
   - Folder: `/ (root)`
5. Click **Save**
6. Wait 1-2 minutes for GitHub to build the site

### Issue 2: Files Not Pushed to GitHub

**Check:**
```bash
git status
git log --oneline -5
```

**Solution:**
If files aren't pushed:
```bash
git add .
git commit -m "Add project files"
git push -u origin main
```

### Issue 3: Wrong URL

**Correct URL format:**
```
https://fahimehorvatinia.github.io/Group20-Data-Mining-Project/results.html
```

**Note:** 
- Username must match exactly (case-sensitive)
- Repository name must match exactly
- Use `/` not `\` in the path

### Issue 4: Repository is Private

**Solution:**
- GitHub Pages works with private repos (if you have GitHub Pro/Team)
- Or make the repository public (Settings → Change visibility)

### Issue 5: Branch Name Mismatch

**Check your branch:**
```bash
git branch
```

**Solution:**
- If your branch is `master`, either:
  - Rename to `main`: `git branch -M main`
  - Or select `master` in GitHub Pages settings

### Issue 6: File Not in Root Directory

**Verify:**
```bash
ls -la results.html
```

**Solution:**
- `results.html` must be in the root of your repository
- Not in a subfolder

## Step-by-Step Setup

### Step 1: Verify Files Are Pushed

```bash
# Check what's on GitHub
git ls-remote origin main

# If empty, push:
git push -u origin main
```

### Step 2: Enable GitHub Pages

1. Repository → Settings → Pages
2. Source: `main` branch, `/ (root)` folder
3. Click Save
4. Wait for green checkmark

### Step 3: Check Build Status

- Go to **Actions** tab in your repository
- Look for "pages build and deployment"
- Should show green checkmark when complete

### Step 4: Access Your Site

After 1-2 minutes:
```
https://fahimehorvatinia.github.io/Group20-Data-Mining-Project/results.html
```

## Quick Fix Script

Run this to check everything:

```bash
#!/bin/bash
echo "Checking repository status..."
echo "Branch: $(git branch --show-current)"
echo "Remote: $(git remote get-url origin)"
echo ""
echo "Files to push:"
git status --short
echo ""
echo "Recent commits:"
git log --oneline -3
echo ""
echo "If files need to be pushed, run:"
echo "  git add ."
echo "  git commit -m 'Add files'"
echo "  git push -u origin main"
```

## Alternative: Create index.html

If you want the main URL to work (without `/results.html`):

Create `index.html`:
```html
<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="refresh" content="0; url=results.html">
    <title>ESC-50 Project Results</title>
</head>
<body>
    <p>Redirecting to <a href="results.html">results.html</a></p>
</body>
</html>
```

Then:
```bash
git add index.html
git commit -m "Add index redirect"
git push
```

Your site will be at:
```
https://fahimehorvatinia.github.io/Group20-Data-Mining-Project/
```

## Still Not Working?

1. **Check repository exists:**
   - Visit: `https://github.com/fahimehorvatinia/Group20-Data-Mining-Project`
   - Should see your files

2. **Check Pages settings:**
   - Settings → Pages
   - Should show: "Your site is published at..."

3. **Wait longer:**
   - First deployment can take 5-10 minutes
   - Subsequent updates are faster (1-2 minutes)

4. **Check Actions tab:**
   - Should show successful deployment
   - If failed, check error message

5. **Try different browser/incognito:**
   - Sometimes browser cache causes issues

## Verification Checklist

- [ ] Repository exists on GitHub
- [ ] Files are pushed to `main` branch
- [ ] GitHub Pages is enabled (Settings → Pages)
- [ ] Source branch is `main` (or `master`)
- [ ] Source folder is `/ (root)`
- [ ] `results.html` is in root directory
- [ ] Waited 1-2 minutes after enabling
- [ ] Checked Actions tab for build status

