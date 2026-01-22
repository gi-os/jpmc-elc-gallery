# Deployment Instructions

## Quick Start - GitHub Pages Deployment

Follow these steps to deploy your JPMC photo gallery to GitHub Pages:

### Step 1: Create GitHub Repository

1. Go to https://github.com/new
2. Repository name: `jpmc-elc-gallery` (or your preferred name)
3. Description: "JPMC ELC Photo Gallery - Password Protected"
4. Keep it **Private** (recommended for client work)
5. **DO NOT** initialize with README, .gitignore, or license
6. Click "Create repository"

### Step 2: Push Your Code

Copy and paste these commands in your terminal (from the jpmc-gallery directory):

```bash
git remote add origin https://github.com/YOUR_USERNAME/jpmc-elc-gallery.git
git push -u origin main
```

Replace `YOUR_USERNAME` with your actual GitHub username.

### Step 3: Enable GitHub Pages

1. Go to your repository on GitHub
2. Click "Settings" tab
3. Scroll down and click "Pages" in the left sidebar
4. Under "Source", select branch: **main**
5. Keep folder as **/ (root)**
6. Click "Save"

### Step 4: Access Your Site

After 1-2 minutes, your site will be live at:
```
https://YOUR_USERNAME.github.io/jpmc-elc-gallery/
```

## Password Information

**Default Password:** `jpmc2026`

Share this password with authorized users only.

## Customization

### Change Password
Edit `index.html`, line 336:
```javascript
const correctPassword = 'your-new-password';
```

Then commit and push:
```bash
git add index.html
git commit -m "Update password"
git push
```

### Update Photos
1. Add/remove photos in the `photos/` folders
2. Run: `python3 generate_paths.py`
3. Commit and push changes

## Troubleshooting

**Site not loading?**
- Wait 2-3 minutes after enabling GitHub Pages
- Check GitHub Actions tab for deployment status
- Ensure repository is not empty

**Images not showing?**
- Check that photos are committed to repository
- Verify paths in browser console (F12)

**Need help?**
- Check GitHub Pages documentation: https://docs.github.com/en/pages
- Verify all files are pushed: `git status`

## Security Notes

- This is client-side password protection (basic security)
- For sensitive content, consider using GitHub's private pages or server-side authentication
- The repository should be kept private to protect client assets
