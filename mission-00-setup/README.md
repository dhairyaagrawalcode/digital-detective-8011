# Mission 0 — Create your GitHub workspace

## 1. Task / objective
The objective of Mission 0 is to set up a clean, structured workspace for the Digital Detective assignment. This involves verifying prerequisite tools (Python 3 and Git), creating the required directory structure for all nine missions (Mission 0 through Mission 8) along with an `evidence/` directory, preparing the root `README.md`, initializing a Git repository, and linking it to a public GitHub remote repository named `digital-detective-8011`.

## 2. Work completed
- Checked and confirmed the local installation of Python 3 and Git via the Terminal.
- Created the project repository folder named `digital-detective-8011` based on the naming convention (assignment name + hyphen + last 4 digits of USN: `8011`).
- Created dedicated directories and placeholder `README.md` files for all missions:
  - `mission-00-setup/README.md`
  - `mission-01-computer-basics/README.md`
  - `mission-02-terminal/README.md`
  - `mission-03-operating-system/README.md`
  - `mission-04-programs/README.md`
  - `mission-05-numbers-data/README.md`
  - `mission-06-git-github/README.md`
  - `mission-07-networking/README.md`
  - `mission-08-final-report/README.md`
  - `evidence/`
- Configured the root `README.md` with the project overview, student details, index table of missions with links to each mission's README, and workflow rules.
- Connected the local repository to GitHub under the remote origin `https://github.com/dhairyaagrawalcode/digital-detective-8011.git`.

## 3. Commands / tools used
- `python3 --version`: Verified the installed version of Python (`Python 3.15.0`).
- `git --version`: Verified the installed version of Git (`git version 2.54.0`).
- `mkdir <folder>`: Created folders for each mission and the evidence directory.
- `touch <file>`: Created initial Markdown documentation files.
- `git init`: Initialized the Git version control repository locally.
- `git remote add origin <url>`: Linked the local Git repository to the remote GitHub repository.
- `git status`: Inspected the working tree status before staging.
- `git add <files>`: Staged initial files for tracking.
- `git commit -m "<message>"`: Committed changes with descriptive messages.
- `git push -u origin main`: Pushed initial commits to GitHub.

## 4. My understanding
A Git repository is a digital storage space tracked by the Git version control system. It records the complete timeline of changes, file modifications, additions, and deletions, enabling safe experimentation, rollback to previous states, and collaboration. 

Organising the project into distinct mission folders provides modularity and clarity. Each mission represents an independent milestone with its own specific learning goals, command explorations, and practical evidence. Keeping them in dedicated folders prevents clutter, ensures file management safety, and allows instructors and peers to evaluate progress incrementally without mixing work from different modules.

## 5. Difficulties faced
Initially, the mission index links in the root `README.md` were placeholder links all pointing to `mission-00-setup/README.md` instead of their respective mission folders, and the root README required full navigation links and description updates.

## 6. How I resolved them
Updated the links in the root `README.md` so that each mission entry correctly hyperlinks to its own directory (`./mission-01-computer-basics/README.md`, `./mission-02-terminal/README.md`, etc.), verified all paths exist on disk, and tested navigation locally.

## 7. Evidence / files
- Repository structure verified:
  ```
  digital-detective-8011/
  ├── README.md
  ├── evidence/
  ├── mission-00-setup/README.md
  ├── mission-01-computer-basics/README.md
  ├── mission-02-terminal/README.md
  ├── mission-03-operating-system/README.md
  ├── mission-04-programs/README.md
  ├── mission-05-numbers-data/README.md
  ├── mission-06-git-github/README.md
  ├── mission-07-networking/README.md
  └── mission-08-final-report/README.md
  ```
- Tool verification outputs:
  - Python: `Python 3.15.0`
  - Git: `git version 2.54.0`

## 8. Commit details
- Commit message: `Set up Digital Detective mission structure`
- Status: Staged, committed, and pushed to `main` branch on GitHub.
