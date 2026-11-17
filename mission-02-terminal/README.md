# Mission 2 — Become comfortable with the Terminal

## 1. Task / objective
The goal of this mission was to learn how to use the command line (Terminal). I practiced basic commands for checking current location, listing files, creating folders and text files, copying, renaming, viewing file contents, using command flags, connecting commands using pipes (`|`), and checking how package managers work on macOS.

## 2. Work completed

### Task 2.1 — Explore basic Terminal operations

| Operation / command name | What it does | What I observed |
| :--- | :--- | :--- |
| **Current-directory display** (`pwd`) | Prints the full path of the folder I am currently working in. | Terminal printed the full directory path starting from `/Users/...` to my assignment folder. |
| **Directory listing** (`ls`) | Shows the names of files and folders inside the current folder. | Showed all my mission folders (`mission-00`, `mission-01`, etc.) and the README file. |
| **Detailed listing** (`ls -l`) | Shows files with extra details like file permissions, owner, file size, and last modified date. | Displayed each item on a separate line with permission letters (`drwxr-xr-x`), file sizes, and dates. |
| **Change directory** (`cd ..`) | Moves my terminal location up one level into the parent directory. | The terminal prompt changed to show I was now in the parent folder. Running `pwd` confirmed the new path. |
| **Create directory** (`mkdir terminal-practice`) | Makes a brand new folder with the given name. | A new folder named `terminal-practice` appeared in my project. |
| **Create empty file** (`touch note.txt`) | Creates a new empty file if it doesn't exist yet. | An empty file called `note.txt` was created inside my practice folder. |
| **Copy file** (`cp note.txt note_backup.txt`) | Makes an exact duplicate of a file with a new name. | I had two separate files with the same content: `note.txt` and `note_backup.txt`. |
| **Move / rename file** (`mv note_backup.txt note_backup_renamed.txt`) | Renames a file or moves it to another location. | `note_backup.txt` was renamed to `note_backup_renamed.txt`. The old name was gone. |
| **Display file contents** (`cat note.txt`) | Prints whatever text is inside the file directly onto the terminal screen. | Terminal displayed both lines of text that I had written into `note.txt`. |

---

### Task 2.2 — Practise file changes safely
Inside the `terminal-practice` folder:
- Created `note.txt` and added one line using `echo "First line of practice notes." > note.txt`.
- Added a second line without deleting the first line using `echo "Second line of practice notes appended." >> note.txt`.
- Displayed the file using `cat note.txt` to confirm both lines were there.
- Made a copy using `cp note.txt note_backup.txt`.
- Renamed the backup using `mv note_backup.txt note_backup_renamed.txt`.

#### Answers to questions:
- **What is the difference between replacing a file's contents and adding text to the end?**  
  Using a single arrow `>` overwrites whatever was already inside the file, replacing all old text. Using double arrows `>>` appends the new text at the end of the file while leaving the existing content untouched.
- **What is the difference between copying a file and moving a file?**  
  Copying (`cp`) leaves the original file where it was and creates a second duplicate copy. Moving (`mv`) changes the file's name or moves it to a new folder, so only one file remains in the end.
- **What information does the current-directory display provide?**  
  `pwd` gives you the exact absolute path from the root folder (`/`) to the folder you are currently in. This prevents you from accidentally modifying or deleting files in the wrong location.
- **Why is a directory-listing operation useful?**  
  `ls` lets you see what files and folders are present in your current folder without having to switch to a graphical file manager like Finder or File Explorer.

---

### Task 2.3 — Understand flags and pipes
- **Comparing `ls` and `ls -lah`**:  
  When I ran plain `ls`, it only gave me simple names of the files side by side. When I ran `ls -lah`, the flags changed the output completely:
  - `-l` showed a long detailed list with permissions and dates.
  - `-a` showed all files including hidden files that start with a dot (like `.git`).
  - `-h` showed file sizes in easy units like KB, MB instead of huge byte numbers.
- **Pipes (`ls -lah | head -n 5`)**:  
  The pipe symbol `|` takes the output of the first command and feeds it directly as input to the second command. Here, `ls -lah` generated the detailed list of files, and `head -n 5` took that list and displayed only the first 5 lines.

---

### Task 2.4 — Understand package managers
- **Package Manager checked**: Homebrew (`brew`)
- **Version observed**: `Homebrew 7.0.13`
- **Why package managers are useful**:  
  A package manager like Homebrew on Mac is like an App Store for developers. Instead of searching Google for software, downloading `.dmg` or `.zip` files, dragging them to applications, and managing updates manually, you can just type a single command like `brew install <package>` in Terminal. It automatically downloads the tool, sets up any required libraries, and keeps everything up to date.

---

## 3. Commands / tools used
- `pwd`, `ls`, `ls -l`, `ls -lah` - Checked current folder path and listed files with various options.
- `cd`, `cd ..` - Navigated folders.
- `mkdir` - Created the `terminal-practice` directory.
- `touch`, `echo >`, `echo >>` - Created and appended text into files.
- `cat` - Printed file contents to terminal.
- `cp`, `mv` - Copied and renamed practice files.
- `|` and `head -n 5` - Filtered command output using a pipe.
- `brew --version`, `brew list --formula` - Inspected Homebrew and its installed packages.

## 4. My understanding
Using the Terminal felt a bit scary at first because there are no buttons to click, but once I learned commands like `pwd`, `ls`, `cd`, and `cat`, it actually felt much faster than clicking around with a mouse. Learning how `>` overwrites and `>>` appends was very important so I don't accidentally wipe out my files. The pipe command `|` was really cool because it shows how small terminal tools can work together to filter data.

## 5. Difficulties faced
When practicing appending text, I had to be careful not to type single `>` by mistake, which would have erased the first line I had written.

## 6. How I resolved them
I double checked my command before pressing Enter and made sure to use `>>` for adding the second line. Then I used `cat note.txt` immediately to verify that both lines were present.

## 7. Evidence / files
- `terminal-practice/` folder containing:
  - `note.txt` (has both the first line and the appended second line)
  - `note_backup_renamed.txt` (the renamed copy)
- `mission-02-terminal/README.md`

## 8. Commit details
- Commit message: `Complete Terminal and file management mission`
- Pushed to: `main` branch on GitHub.
