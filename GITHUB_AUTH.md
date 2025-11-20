# GitHub Authentication Guide

## Authentication Options

You have two options for pushing to GitHub:

### Option 1: HTTPS (Recommended - Easier)

**Already configured!** The remote is now set to use HTTPS.

#### First Time Setup:
1. When you run `git push`, GitHub will prompt for:
   - **Username**: Your GitHub username (`fahimehorvatinia`)
   - **Password**: Use a **Personal Access Token** (NOT your GitHub password)

#### Create Personal Access Token:
1. Go to: https://github.com/settings/tokens
2. Click "Generate new token" → "Generate new token (classic)"
3. Give it a name: "Group20-Data-Mining-Project"
4. Select scopes: Check `repo` (full control of private repositories)
5. Click "Generate token"
6. **Copy the token immediately** (you won't see it again!)
7. Use this token as your password when pushing

#### Push:
```bash
./push_to_github.sh
# Or manually:
git push -u origin main
```

---

### Option 2: SSH (More Secure, But Requires Setup)

If you prefer SSH:

#### Step 1: Generate SSH Key
```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
# Press Enter to accept default location
# Optionally set a passphrase
```

#### Step 2: Add SSH Key to GitHub
```bash
# Display your public key
cat ~/.ssh/id_ed25519.pub

# Copy the output, then:
# 1. Go to: https://github.com/settings/keys
# 2. Click "New SSH key"
# 3. Paste your public key
# 4. Click "Add SSH key"
```

#### Step 3: Switch Remote to SSH
```bash
git remote set-url origin git@github.com:fahimehorvatinia/Group20-Data-Mining-Project.git
```

#### Step 4: Test Connection
```bash
ssh -T git@github.com
# Should say: "Hi fahimehorvatinia! You've successfully authenticated..."
```

---

## Quick Push (HTTPS - Current Setup)

```bash
./push_to_github.sh
```

When prompted:
- **Username**: `fahimehorvatinia`
- **Password**: Your Personal Access Token

---

## Troubleshooting

### "Repository not found"
- Make sure the repository exists on GitHub
- Check the repository name is correct: `Group20-Data-Mining-Project`
- Verify you have access to the repository

### "Authentication failed"
- For HTTPS: Make sure you're using a Personal Access Token, not your password
- For SSH: Make sure your SSH key is added to GitHub

### "Permission denied"
- Check repository permissions
- Verify you're the owner or have write access

### "Nothing to commit"
- Make sure you've added files: `git add .`
- Make sure you've committed: `git commit -m "message"`

---

## Current Setup

Remote is configured for HTTPS. Ready to push (just need authentication).

Run: `./push_to_github.sh`

