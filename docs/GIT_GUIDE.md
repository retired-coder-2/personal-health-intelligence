# 🌲 Git Quick Reference Guide

Your personal cheat sheet for Git commands.

---

## 🎯 **Git in 30 Seconds**

Git is a **time machine** for your code. It saves snapshots (commits) so you can:
- Go back to any previous version
- See what changed
- Collaborate without overwriting each other's work

---

## 🚀 **Daily Git Workflow**

```bash
# 1. See what changed
git status

# 2. Add files to stage (prepare for snapshot)
git add .                    # Add all files
git add filename.py          # Add specific file

# 3. Take snapshot (commit)
git commit -m "Your message describing what you did"

# 4. Upload to GitHub (backup + portfolio)
git push origin main
```

That's it! Those 4 commands are 90% of what you'll do.

---

## 📸 **Making Your First Commit** (Step by Step)

### Step 1: Check Status
```bash
git status
```
**What it shows:** Files that changed (red = not staged, green = staged)

### Step 2: Stage Files
```bash
git add .
```
**What it does:** Marks files to include in next snapshot  
**Think of it as:** Putting items in a shopping cart before checkout

### Step 3: Commit (Take Snapshot)
```bash
git commit -m "Initial project setup"
```
**What it does:** Saves current state with a description  
**Think of it as:** Saving your game with a note about where you are

### Step 4: Push to GitHub
```bash
git push origin main
```
**What it does:** Uploads your commits to GitHub  
**Think of it as:** Cloud backup + showing your work to the world

---

## 🔍 **Common Git Commands**

### Viewing History
```bash
# See all commits
git log

# See last 5 commits (prettier)
git log --oneline -5

# See what changed in last commit
git show
```

### Checking Changes
```bash
# See what changed (not staged yet)
git diff

# See what's staged for commit
git diff --staged
```

### Undoing Mistakes
```bash
# Unstage a file (keep changes)
git reset filename.py

# Undo changes in a file (CAREFUL - permanent!)
git checkout -- filename.py

# Undo last commit (keep changes)
git reset HEAD~1

# Undo last commit (delete changes - CAREFUL!)
git reset --hard HEAD~1
```

### Branches (Parallel Universes)
```bash
# See all branches
git branch

# Create new branch
git branch feature-name

# Switch to branch
git checkout feature-name

# Create and switch in one command
git checkout -b feature-name

# Merge branch into current branch
git merge feature-name

# Delete branch
git branch -d feature-name
```

---

## 🐙 **GitHub Operations**

### First Time Setup
```bash
# Connect your local repo to GitHub
git remote add origin https://github.com/YOUR_USERNAME/personal-health-intelligence.git

# Push and set upstream
git push -u origin main
```

### Daily Operations
```bash
# Download latest changes
git pull origin main

# Upload your changes
git push origin main

# Clone someone else's project
git clone https://github.com/username/project.git
```

---

## 📝 **Writing Good Commit Messages**

### Format
```
<type>: <short description>

<optional longer description>

<optional footer>
```

### Types
- `feat`: New feature
- `fix`: Bug fix  
- `docs`: Documentation changes
- `test`: Adding tests
- `refactor`: Code cleanup
- `style`: Formatting
- `chore`: Maintenance

### Examples

**Good:**
```
feat: add file scanning with metadata extraction

Implemented scan_folder() function that walks through
directories recursively and extracts file metadata
including size, type, and dates.
```

**Bad:**
```
updated stuff
```

---

## 🚨 **Common Mistakes & Fixes**

### "I committed to the wrong branch!"
```bash
# Create new branch with current changes
git branch correct-branch

# Go back to previous branch
git checkout previous-branch

# Remove the wrong commit
git reset HEAD~1 --hard

# Switch to correct branch
git checkout correct-branch
```

### "I need to change my last commit message!"
```bash
git commit --amend -m "New message"
```

### "I accidentally committed a secret/password!"
```bash
# First, change the password immediately!
# Then remove from Git history (advanced - be careful)
git filter-branch --force --index-filter \
  'git rm --cached --ignore-unmatch path/to/secret/file' \
  --prune-empty --tag-name-filter cat -- --all
```

### "I want to undo everything and start over!"
```bash
# Reset to last commit (CAREFUL - deletes changes!)
git reset --hard HEAD

# Reset to specific commit
git reset --hard COMMIT_HASH
```

---

## 🎮 **Git Gaming Analogy**

| Git Command | Gaming Equivalent |
|------------|------------------|
| `git add` | Put items in quick-access inventory |
| `git commit` | Save game at checkpoint |
| `git push` | Upload save to cloud |
| `git pull` | Download latest save |
| `git branch` | Parallel universe / New Game+ |
| `git merge` | Combine two save files |
| `git reset` | Load previous save |
| `git log` | View save history |

---

## 🔐 **Git Configuration**

### One-Time Setup
```bash
# Set your name (appears on all commits)
git config --global user.name "Your Name"

# Set your email (should match GitHub)
git config --global user.email "your.email@example.com"

# Set default editor
git config --global core.editor "code --wait"  # VS Code

# Set default branch name
git config --global init.defaultBranch main

# See all settings
git config --list
```

---

## 💡 **Pro Tips**

1. **Commit Often** - Small, frequent commits are better than huge ones
2. **Write Descriptive Messages** - Future you will thank you
3. **Pull Before Push** - Avoids conflicts
4. **Branch for Features** - Keep main branch clean
5. **Don't Commit Secrets** - Use .env files (in .gitignore)
6. **Test Before Committing** - Make sure code works

---

## 📚 **Learn More**

- Interactive Tutorial: https://learngitbranching.js.org/
- Official Docs: https://git-scm.com/doc
- GitHub Guides: https://guides.github.com/

---

**Remember:** Everyone makes Git mistakes. The important part is learning how to fix them! 🚀
