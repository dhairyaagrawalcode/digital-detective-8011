# Mission 6 — Git and GitHub

## 1. Task / objective
The goal of this mission was to learn how Git and GitHub work together for version control and teamwork. I practiced inspecting git status, staging and committing changes, creating a separate feature branch (`update-about`), updating my root README with a learning section, pushing the branch to GitHub, opening and merging a Pull Request, pulling the merged changes back to my local machine, and writing a glossary of common Git commands.

## 2. Work completed

### Task 6.1 — Understand the basic Git workflow

| Git operation | What it does in your own words |
| :--- | :--- |
| **Check repository status** (`git status`) | Shows which files have been modified, which files are staged for commit, and which files are untracked. |
| **Stage selected changes** (`git add <file>`) | Marks specific modified files to be included in the next commit snapshot. |
| **Create a commit** (`git commit -m "<message>"`) | Saves the staged changes permanently in your local Git history with an explanatory message. |
| **View commit history** (`git log` / `git log --oneline`) | Displays the list of previous commits, showing their commit ID, author, and commit message. |

#### Difference between staging a change and committing it:
Staging (`git add`) is like putting files into a staging area or shopping cart—it lets you choose exactly which files you want to save together. Committing (`git commit`) is like checking out and taking a permanent snapshot of those staged files in Git's history book.

---

### Task 6.2 — Create and use a branch
- Created and switched to a new branch called `update-about`:
  ```bash
  git checkout -b update-about
  ```
- Opened the root `README.md` and added a section titled `## My Learning` describing 3 things I learned so far.
- Staged the change using `git add README.md` and committed it with the message:
  ```bash
  git commit -m "Add My Learning section to root README"
  ```
- Pushed the new branch to GitHub:
  ```bash
  git push -u origin update-about
  ```

---

### Task 6.3 — Create a Pull Request
1. Opened the repository on GitHub and saw the prompt to compare and open a Pull Request for branch `update-about`.
2. Created **Pull Request #1** titled *"Add My Learning section to root README"*.
3. Added a short description explaining the new learning section in the root README.
4. Reviewed the diff to confirm only the intended lines were changed.
5. Merged the Pull Request into the `main` branch on GitHub.
6. Switched back to `main` locally and pulled the merged changes:
   ```bash
   git checkout main
   git pull origin main
   ```

#### Why branches and Pull Requests are useful:
A **branch** lets you work on a new feature or change without touching the stable `main` code. If you make a mistake, it only affects your branch. A **Pull Request** lets other teammates look over your changes, leave comments, and test the code before it is merged into the main project.

---

### Task 6.4 — Build your Git command glossary

| Git operation | One-line explanation in your own words |
| :--- | :--- |
| **Initialise a repository** | `git init` creates a new local Git repository in the current folder. |
| **Check status** | `git status` shows which files are modified, staged, or untracked. |
| **Stage changes** | `git add` puts modified files into the staging area ready to be committed. |
| **Commit changes** | `git commit -m "..."` saves a permanent snapshot of staged files with a message. |
| **View history** | `git log --oneline` shows a summary list of past commits. |
| **Create or list branches** | `git branch` lists existing branches or makes a new branch when given a name. |
| **Switch branches** | `git checkout <branch>` or `git switch <branch>` switches to another branch. |
| **Publish changes** | `git push` uploads your local commits to the remote repository on GitHub. |
| **Retrieve remote changes** | `git pull` downloads new commits from GitHub and merges them into your local branch. |

---

## 3. Commands / tools used
- `git status`, `git add`, `git commit` - Used for daily staging and committing.
- `git checkout -b update-about` - Created and switched to the feature branch.
- `git push -u origin update-about` - Pushed the branch to GitHub.
- GitHub web interface & `gh pr` - Created and merged Pull Request #1.
- `git pull origin main` - Brought remote changes down to my local machine.

## 4. My understanding
Before this mission, I thought Git and GitHub were the same thing. Now I understand that Git is the version control tool running locally on my computer, while GitHub is a website that hosts the Git repository online so you can share code and collaborate. Working with branches and Pull Requests made me realize how teams work together on software without overwriting each other's work.

## 5. Difficulties faced
When I merged the Pull Request on GitHub, my local terminal still didn't have the new merge commit on the local `main` branch.

## 6. How I resolved them
I ran `git checkout main` and then `git pull origin main`. This brought down the merged commit from GitHub, and my local files were immediately updated.

## 7. Evidence / files
- Remote feature branch: `update-about`
- Pull Request #1: [https://github.com/dhairyaagrawalcode/digital-detective-8011/pull/1](https://github.com/dhairyaagrawalcode/digital-detective-8011/pull/1) (Merged into `main`).
- `mission-06-git-github/README.md`.

## 8. Commit details
- Commit message: `Complete Git and GitHub collaboration mission`
- Pushed to: `main` branch on GitHub.
