# Mission 6 — Git and GitHub

## 1. Task / objective
The objective of Mission 6 is to master collaborative version control using Git and GitHub. This includes understanding the fundamental Git workflow (working directory, staging area, local repository), branching strategies, creating and publishing feature branches, opening and managing a GitHub Pull Request (PR), pulling remote changes back to the local repository, and compiling an essential Git command glossary.

---

## 2. Work completed

### Task 6.1 — Understand the basic Git workflow

| Git Operation | What it does in your own words |
| :--- | :--- |
| **Check repository status** (`git status`) | Inspects the current working tree and staging area, identifying untracked files, modified tracked files, and staged changes ready for commit. |
| **Stage selected changes** (`git add <file>`) | Adds specific file modifications to the Git staging index, curating exactly which changes will be bundled into the next snapshot. |
| **Create a commit** (`git commit -m "<msg>"`) | Records an immutable, timestamped snapshot of staged files into the local repository database with a descriptive message and unique commit hash. |
| **View commit history** (`git log` / `git log --oneline`) | Displays the chronological log of previous commits, showing author details, commit hashes, dates, and commit descriptions. |

#### Difference Between Staging a Change and Committing It
Staging a change (`git add`) acts as an intermediate preparation step: it places selected modifications into a temporary staging area (index), allowing you to carefully organize which files or lines of code belong together. In contrast, committing (`git commit`) seals whatever is currently staged into a permanent, version-controlled snapshot in the repository history. Staging is like packing items into a shipping box; committing is sealing and stamping the box with a tracking number.

---

### Task 6.2 — Create and use a branch
- Created and switched to a new branch named `update-about`:
  ```bash
  git checkout -b update-about
  ```
- Edited the root `README.md` to add the section titled `## My Learning` detailing computer fundamentals, terminal operations, and data representation.
- Staged and committed the changes on the branch:
  ```bash
  git add README.md
  git commit -m "Add My Learning section to root README"
  ```
- Published the branch to GitHub:
  ```bash
  git push -u origin update-about
  ```

---

### Task 6.3 — Create a Pull Request
1. Created Pull Request #1 targeting `main` from branch `update-about` on GitHub:
   - **PR Title**: `Add My Learning section to root README`
   - **PR Description**: Added the "My Learning" overview section highlighting key learnings from computer basics, terminal operations, operating systems, and data representation.
   - **PR URL**: [https://github.com/dhairyaagrawalcode/digital-detective-8011/pull/1](https://github.com/dhairyaagrawalcode/digital-detective-8011/pull/1)
2. Reviewed the file diff on GitHub and completed the merge into `main`:
   - **Merge status**: Successfully merged (`✓ Merged pull request #1`).
3. Returned to local project, switched to `main`, and pulled down the merged commit:
   ```bash
   git checkout main
   git pull origin main
   ```

#### Importance of Branches and Pull Requests
- **Branch**: An independent, lightweight pointer to a commit that isolates experimental or feature work from the production `main` branch. This ensures developers can write, test, and iterate without destabilizing functional code.
- **Pull Request (PR)**: A structured peer-review workflow on collaboration platforms like GitHub where proposed branch changes are discussed, visually diffed, checked by automated continuous integration (CI) tests, and approved before being merged into the primary branch.

---

### Task 6.4 — Build your Git command glossary

| Git Operation | One-Line Explanation in Own Words |
| :--- | :--- |
| **Initialise a repository** | `git init` creates an empty local Git repository and initializes the internal `.git` tracking metadata. |
| **Check status** | `git status` shows the state of working directory files (untracked, modified, staged) relative to the repository. |
| **Stage changes** | `git add <path>` moves modified file contents into the staging area (index) for inclusion in the upcoming commit. |
| **Commit changes** | `git commit -m "<msg>"` writes all staged modifications into a permanent, tracked snapshot in repository history. |
| **View history** | `git log --oneline` prints the reverse-chronological list of all committed snapshots and their commit messages. |
| **Create or list branches** | `git branch` displays existing branch names or creates a new branch pointer when given a name argument. |
| **Switch branches** | `git switch <branch>` / `git checkout <branch>` switches HEAD and the working directory files to the specified branch. |
| **Publish changes** | `git push <remote> <branch>` uploads local branch commits to the remote hosting server (e.g., GitHub). |
| **Retrieve remote changes** | `git pull <remote> <branch>` downloads remote branch commits and immediately merges them into the local branch. |

---

## 3. Commands / tools used
- `git status`: Inspected workspace status.
- `git checkout -b update-about`: Created and switched to the feature branch.
- `git add README.md`: Staged file modifications.
- `git commit -m "..."`: Committed feature branch changes.
- `git push -u origin update-about`: Published feature branch to remote GitHub.
- `gh pr create`: Created Pull Request #1 on GitHub via the GitHub CLI.
- `gh pr merge`: Merged Pull Request #1 into `main`.
- `git checkout main` & `git pull origin main`: Synchronized local `main` with remote merged state.

---

## 4. My understanding
Version control is the bedrock of modern software engineering. Rather than manually copying files with names like `project_final_v2_edit.zip`, Git creates a cryptographic Directed Acyclic Graph (DAG) of project states. Branching allows parallel feature development without risk, while GitHub Pull Requests transform code changes into transparent, reviewable collaboration checkpoints.

---

## 5. Difficulties faced
Ensuring local `main` was cleanly synchronized after merging Pull Request #1 on the remote GitHub repository without merge conflicts.

---

## 6. How I resolved them
Checked out local `main` and ran `git pull origin main`, which completed a clean fast-forward merge of the PR commit without any conflict.

---

## 7. Evidence / files
- Pull Request #1 URL: [https://github.com/dhairyaagrawalcode/digital-detective-8011/pull/1](https://github.com/dhairyaagrawalcode/digital-detective-8011/pull/1)
- Remote Branch: `update-about`
- Root `README.md` updated with "My Learning" section.
- `mission-06-git-github/README.md`: Documented Git workflow, PR evidence, and Git glossary.

---

## 8. Commit details
- Commit message: `Complete Git and GitHub collaboration mission`
- Status: Staged, committed, and pushed to `main` branch on GitHub.
