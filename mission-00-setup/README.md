# Mission 0 — Create your GitHub workspace

## 1. Task / objective
The goal of this mission was to get our assignment workspace set up properly. I had to check that Python 3 and Git were installed on my laptop, create the project folder following the naming convention (`digital-detective-` followed by the last four digits of my USN: `8011`), create all the mission folders and README files, write the main root README, and link everything to a public GitHub repository.

## 2. Work completed
- Checked my Terminal to verify Python 3 and Git versions.
- Created the main folder named `digital-detective-8011`.
- Made all the required mission directories and placeholder markdown files:
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
- Set up the main `README.md` in the root folder with an index pointing to each mission.
- Initialised Git locally and connected it to my GitHub repository at `https://github.com/dhairyaagrawalcode/digital-detective-8011`.

## 3. Commands / tools used
- `python3 --version` - Checked my Python version (got Python 3.15.0).
- `git --version` - Checked my Git version (got git version 2.54.0).
- `mkdir` - Used in terminal to make directories for each mission.
- `touch` - Created empty README.md files inside the folders.
- `git init` - Initialized the local git repository in my project folder.
- `git remote add origin https://github.com/dhairyaagrawalcode/digital-detective-8011.git` - Linked my local repo to my GitHub repo.
- `git status` - Checked which files were tracked and untracked.
- `git add .` - Staged the files for committing.
- `git commit -m "..."` - Saved my changes with a commit message.
- `git push -u origin main` - Uploaded my initial commit to GitHub.

## 4. My understanding
A Git repository is basically a project folder where Git tracks every change you make to files over time. It lets you save snapshots of your progress so you can review what you did or roll back if something breaks.

Having separate folders for each mission keeps things clean and organized. Instead of putting all files in one big folder where it's hard to find anything, having folders from `mission-00` to `mission-08` lets me focus on one topic at a time and makes it easy for the teacher to review each mission step by step.

## 5. Difficulties faced
When I first wrote the links in the root `README.md`, I noticed all the links were accidentally pointing to `./mission-00-setup/README.md` because of copy-pasting the markdown syntax.

## 6. How I resolved them
I edited `README.md` and fixed each link path so that `mission-01` points to `./mission-01-computer-basics/README.md`, `mission-02` points to `./mission-02-terminal/README.md`, and so on. Then I clicked each link in the preview to make sure they opened the right files.

## 7. Evidence / files
- Project folder structure:
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
- Tool checks:
  - Python: `Python 3.15.0`
  - Git: `git version 2.54.0`

## 8. Commit details
- Commit message: `Set up Digital Detective mission structure`
- Pushed to: `main` branch on GitHub.
