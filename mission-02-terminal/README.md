# Mission 2 — Become comfortable with the Terminal

## 1. Task / objective
The objective of Mission 2 is to gain hands-on proficiency with the command-line interface (CLI) in Terminal. This includes navigating directories, inspecting files, executing safe file-creation, copying, renaming, and reading operations, understanding command options/flags and Unix pipeline mechanisms (`|`), and exploring package managers such as Homebrew on macOS.

---

## 2. Work completed

### Task 2.1 — Explore basic Terminal operations

| Operation / Command Name | What it does | What I observed (privacy-safe) |
| :--- | :--- | :--- |
| **Current-directory display** (`pwd`) | Prints the absolute pathname of the current working directory from the root filesystem. | Displayed the active path: `.../Projects/digital-detective-8011` |
| **Directory listing** (`ls`) | Lists the non-hidden file and folder names contained in the current directory. | Outputted names of mission folders, README, evidence, and practice folders across columns. |
| **Detailed listing** (`ls -l`) | Lists files and folders in long format showing file permissions, number of hard links, owner, group, byte size, modification timestamp, and name. | Displayed entries line-by-line with mode strings like `drwxr-xr-x` and byte sizes. |
| **Change directory** (`cd ..` / `cd -`) | Changes the shell's active working directory to the parent folder (`..`) or previous directory (`-`). | The current working path changed to the parent workspace directory, and shell prompt updated accordingly. |
| **Create directory** (`mkdir terminal-practice`) | Creates a new directory at the specified path if it does not already exist. | Created the dedicated practice directory `terminal-practice` without altering existing files. |
| **Create empty file** (`touch note.txt`) | Updates file access/modification timestamps, or creates an empty file if it doesn't exist. | An empty file `note.txt` of 0 bytes was generated inside `terminal-practice`. |
| **Copy file** (`cp note.txt note_backup.txt`) | Duplicates the contents of a source file into a newly created or overwritten destination file. | A distinct, duplicate file `note_backup.txt` was created with identical content to `note.txt`. |
| **Move / rename file** (`mv note_backup.txt note_backup_renamed.txt`) | Relocates or renames a file or directory in the filesystem without duplicating the underlying data blocks. | The file `note_backup.txt` was renamed to `note_backup_renamed.txt`; the old filename ceased to exist. |
| **Display file contents** (`cat note.txt`) | Concatenates and prints file contents directly to standard output (the terminal window). | Displayed both lines of written text cleanly in the console window. |

---

### Task 2.2 — Practise file changes safely
Within the dedicated `terminal-practice/` folder:
1. Created `note.txt` with an initial line: `echo "First line of practice notes." > note.txt`.
2. Appended a second line without overwriting: `echo "Second line of practice notes appended." >> note.txt`.
3. Verified both lines using `cat note.txt`.
4. Copied to backup: `cp note.txt note_backup.txt`.
5. Renamed backup: `mv note_backup.txt note_backup_renamed.txt`.

#### Conceptual Questions
- **What is the difference between replacing a file's contents and adding text to the end?**  
  Using the single redirect operator `>` overwrites and truncates the existing file content completely from byte 0 with new input. In contrast, using the append redirect operator `>>` preserves existing data and appends the new text stream at the end of the file.
- **What is the difference between copying a file and moving a file?**  
  Copying (`cp`) creates a duplicate file entity in the filesystem, consuming additional storage blocks while keeping the original intact. Moving (`mv`) re-links or renames the file inode within the directory structure, resulting in a single file at the new path or under the new name.
- **What information does the current-directory display provide?**  
  `pwd` (Print Working Directory) provides the complete absolute path from the root directory (`/`) to the exact directory where the shell is currently executing, ensuring safe context before executing relative path commands or file operations.
- **Why is a directory-listing operation useful?**  
  Listing (`ls`) allows the user to inspect directory contents, verify whether expected files and subfolders exist, inspect hidden configuration files (with `-a`), and verify file metadata such as sizes, permissions, and timestamps (with `-l`).

---

### Task 2.3 — Understand flags and pipes

#### Flags Exploration: `ls` vs `ls -lah`
- Running `ls` produces a plain list of visible filenames in multi-column layout with no metadata.
- Running `ls -lah` modifies the command behavior using three combined flags:
  - `-l`: Formats output as a long detailed list showing permissions, ownership, byte size, and timestamps.
  - `-a`: Displays all files, including hidden entries starting with a dot (`.` and `..`, `.git`, etc.).
  - `-h`: Human-readable file sizes (e.g., formatting byte values into `480B`, `3.0K`, `926M`).

#### Unix Pipes Exploration: `ls -lah | head -n 5`
- The pipe symbol (`|`) connects the standard output (`stdout`) of the command on the left directly into the standard input (`stdin`) of the command on the right without writing to a temporary file on disk.
- **Left side (`ls -lah`)**: Generates a complete, detailed stream of all files and directories with metadata.
- **Right side (`head -n 5`)**: Filters the received input stream and terminates after outputting only the first 5 lines (header total and top 4 entries).
- **Benefit**: Pipes enable command composition, combining small, single-purpose Unix tools into powerful data pipelines.

---

### Task 2.4 — Understand package managers
- **Tool Checked**: Homebrew (`brew`)
- **Version**: `Homebrew 7.0.13`
- **Managed Packages Inspected**: Formulae such as `aom`, `boost`, `brotli`, `ca-certificates`, `cowsay`, etc.
- **Why Package Managers are Useful**:  
  A package manager automates the entire lifecycle of software installation, upgrading, dependency resolution, and uninstallation on an operating system. Instead of manually downloading binary archives, compiling source code, configuring library paths, and resolving conflicts, a single package manager command fetches verified packages and their required dependencies in a structured, repeatable way.

---

## 3. Commands / tools used
- `pwd`: Displayed the active working directory.
- `ls`, `ls -l`, `ls -lah`: Inspected directory contents with various flags.
- `cd`: Navigated directory hierarchy.
- `mkdir`: Created directory `terminal-practice`.
- `touch`: Created practice text files.
- `echo ... > file` and `echo ... >> file`: Wrote and appended text.
- `cat`: Outputted text file contents.
- `cp`: Duplicated files for backup.
- `mv`: Renamed backup file safely.
- `|` (pipe) with `head -n 5`: Pipelined output to display top rows.
- `brew --version` & `brew list --formula`: Checked package manager and managed packages.

---

## 4. My understanding
The command-line interface provides direct, high-precision control over the operating system. Understanding the difference between relative and absolute navigation prevents costly mistakes. Flags allow tailoring commands to specific operational needs, while Unix pipelines exemplify modular software design: linking simple, decoupled utilities to filter and transform data streams efficiently. Package managers streamline software administration and dependency handling across developer environments.

---

## 5. Difficulties faced
Ensuring practice file modifications did not inadvertently overwrite repository configuration or root files, and verifying that file listings avoided exposing private hostnames or user identities.

---

## 6. How I resolved them
Confined all experimental file creation, appending, copying, and renaming exclusively inside the isolated `terminal-practice/` directory, and reviewed all output summaries to redact private usernames and paths.

---

## 7. Evidence / files
- Directory: `terminal-practice/`
  - `note.txt` (contains two lines demonstrating write and append)
  - `note_backup_renamed.txt` (verified backup file)
- `mission-02-terminal/README.md`: Complete command reference, answers, and explanations.

---

## 8. Commit details
- Commit message: `Complete Terminal and file management mission`
- Status: Staged, committed, and pushed to `main` branch on GitHub.
