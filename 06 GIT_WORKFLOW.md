# Git & GitHub Workflow - Sprint 01 (Days 3-4)

Deep technical documentation of Git concepts and workflow used in this repository.

---

## 1. How Git Actually Works (Internals)

Git isn't just "save points" - it's a content-addressable file system with three core areas:

 **Working Directory** : your actual files, as you edit them.
 **Staging Area (Index)** : a snapshot of what will go into the next commit.
 **Repository (.git folder)** : the committed history, stored as a graph of objects.

Every commit is a snapshot (not a diff) of the entire project at that point, linked to its parent commit(s) - this is why Git history is a **DAG (Directed Acyclic Graph)**, not a straight line. Branches are just movable pointers (refs) to a specific commit. `HEAD` is a pointer to whichever commit/branch you're currently on.

Git objects (stored as SHA-1/SHA-256 hashes):
 **Blob** : file content
 **Tree** : directory structure (folder snapshot)
 **Commit** : pointer to a tree + metadata (author, message, parent commit)

This is why `git log --oneline --graph` visually shows branching/merging - you're literally viewing the commit DAG.

---

## 2. Repositories

```bash
git init                          # initialize a new local repo (creates .git folder)
git clone <url>                   # copy remote repo + full history locally
git remote add origin <url>       # link local repo to a remote
git remote -v                     # verify remote link (fetch/push URLs)
git remote remove origin          # unlink a remote
```

`origin` is just a convention name for "the remote I cloned from or pushed to" - not a keyword.

---

## 3. Staging & Commits

```bash
git status                        # see untracked/modified/staged files
git diff                          # see unstaged changes line-by-line
git diff --staged                 # see staged changes before committing
git add <file>                    # stage a specific file (intentional staging)
git add -p                        # stage changes interactively, hunk by hunk
git commit -m "message"           # commit staged snapshot
git commit --amend                # edit the last commit (message or content)
git log --oneline                 # compact commit history
git log --oneline --graph --all   # visualize branch/commit structure
```

**Why stage selectively (`git add <file>` not `git add .`)?**
It lets you commit logically related changes together - one topic, one commit - instead of dumping unrelated edits into a single commit. This is exactly why our commit history is one-file-per-commit rather than a single bulk push.

**Commit message convention used in this repo:**
