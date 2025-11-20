# Website Setup Guide

## Creating Your Results Website

Your results website (`results.html`) is already created and ready to use. Here are the options for hosting it:

## Option 1: GitHub Pages (Recommended - Free)

GitHub Pages allows you to host your website directly from your GitHub repository for free.

### Step 1: Enable GitHub Pages

1. Go to your repository on GitHub: `https://github.com/fahimehorvatinia/Group20-Data-Mining-Project`
2. Click on **Settings** (top right of repository page)
3. Scroll down to **Pages** in the left sidebar
4. Under **Source**, select:
   - Branch: `main`
   - Folder: `/ (root)`
5. Click **Save**

### Step 2: Access Your Website

After a few minutes, your website will be available at:
```
https://fahimehorvatinia.github.io/Group20-Data-Mining-Project/results.html
```

Or you can create an `index.html` that redirects to `results.html`:

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

Then your main site URL will be:
```
https://fahimehorvatinia.github.io/Group20-Data-Mining-Project/
```

### Step 3: Update Results

1. Edit `results.html` with your actual results
2. Commit and push:
```bash
git add results.html
git commit -m "Update results"
git push
```
3. Changes will appear on your website within a few minutes

---

## Option 2: Local Viewing

Simply open `results.html` in your web browser:

```bash
# On Linux/Mac
open results.html
# or
xdg-open results.html

# On Windows
start results.html
```

---

## Option 3: Other Hosting Services

You can also host `results.html` on:
- **Netlify** (free): Drag and drop the file
- **Vercel** (free): Connect your GitHub repo
- **GitHub Pages** (recommended - already integrated)

---

## Updating the Website

### Update Results Data

1. Open `results.html` in a text editor
2. Find the `modelResults` array (around line 280)
3. Update with your actual test accuracies:

```javascript
const modelResults = [
    {"name": "Logistic Regression", "member": "Sushama", "raw": 0.45, "norm": 0.52, "sel": 0.48},
    {"name": "KNN", "member": "Sushama", "raw": 0.38, "norm": 0.41, "sel": 0.39},
    // ... update all models with actual results
];
```

4. Save and push to GitHub

### Customize the Website

You can customize:
- Colors: Edit the CSS in the `<style>` section
- Content: Modify the HTML sections
- Chart: Adjust Chart.js settings in the JavaScript section

---

## Website Features

Your website includes:
- Responsive design (works on mobile and desktop)
- Interactive comparison table
- Bar chart visualization
- Team member sections
- Key findings
- Professional styling

---

## Troubleshooting

### Website not loading
- Check that GitHub Pages is enabled in Settings
- Verify `results.html` is in the root directory
- Wait a few minutes for changes to propagate

### Results not showing
- Open browser console (F12) to check for errors
- Verify Chart.js CDN is loading
- Check that `modelResults` array is valid JSON

### Chart not displaying
- Ensure internet connection (Chart.js loads from CDN)
- Check browser console for JavaScript errors
- Verify Chart.js version compatibility

---

## Quick Start

1. **Enable GitHub Pages** (Settings → Pages → Select `main` branch)
2. **Update results** in `results.html`
3. **Push to GitHub**: `git push`
4. **Access website**: `https://fahimehorvatinia.github.io/Group20-Data-Mining-Project/results.html`

That's it! Your website will be live and accessible to anyone.

