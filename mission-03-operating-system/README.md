# Mission 3 — Understand the operating system

## 1. Task / objective
In this mission, I investigated my laptop's operating system environment. I checked system information, active user account, disk storage space, and inspected running processes and their Process IDs (PIDs). I also learned about absolute and relative paths, checked file permissions (`r`, `w`, `x`), and summarized the main jobs an operating system does.

## 2. Work completed

### Task 3.1 — Explore your operating system

| Information explored | What it tells you | Your observation (privacy-safe) |
| :--- | :--- | :--- |
| **Operating system / system details** (`uname -srm`, `sw_vers`) | Shows the OS name, kernel version, and the processor type of my computer. | macOS (Darwin 27.2.0, arm64 Apple Silicon) |
| **Current account identity** (`whoami`) | Shows the username of the user account currently logged into the terminal. | Active user account: `[redacted]` |
| **Available and used storage** (`df -h .`) | Tells how much total space is on the drive, how much is used, and how much is still free. | Total size: `926 GiB`, Used: `210 GiB` (24%), Free: `692 GiB` |
| **System activity snapshot** (`ps aux`) | Shows an instant snapshot of all programs and background services currently running in memory. | Active apps visible like VS Code and background macOS system services like `WindowServer`. |

---

### Task 3.2 — Understand processes

- **What is a process?**  
  A process is simply a program that is currently running in memory. When a program is just sitting on your hard drive or SSD, it is just a saved file. But when you double click it or run it in terminal, the operating system loads it into RAM and starts executing it—at that moment, it becomes a process.
- **What does the PID column represent?**  
  PID stands for **Process Identifier**. It is a unique number that the operating system assigns to each running process so it can keep track of them, manage their resources, or close them if needed.
- **Give two examples of processes that may be running on your computer:**
  1. `Visual Studio Code` (PID e.g. `10318`) - An application process running the text editor window.
  2. `WindowServer` (PID e.g. `404`) - A background system process on macOS that manages and draws all the windows on the screen.

---

### Task 3.3 — Understand paths and permissions

#### Absolute vs Relative Paths
- **Absolute path**: The full path that starts all the way from the root directory (`/`). It works no matter where you currently are in the terminal.
  - *Example from my project*: `/Users/[redacted]/Documents/Projects/digital-detective-8011/terminal-practice/note.txt`
- **Relative path**: A path that starts from your current folder, usually using `.` (this folder) or `..` (parent folder).
  - *Example from my project*: `./terminal-practice/note.txt`

#### File Permissions
When I ran `ls -l terminal-practice/note.txt`, the permissions showed: `-rw-r--r--`

| Permission | Meaning | Example from my practice file |
| :--- | :--- | :--- |
| **r — Read** | Allows reading or viewing the file contents. | As the owner, I have `r`, so I can open and view `note.txt`. |
| **w — Write** | Allows editing, changing, or overwriting the file. | As the owner, I have `w`, so I can add text or modify `note.txt`. |
| **x — Execute** | Allows running the file as a program or script. | As the owner, I have `-` (no `x`), so `note.txt` cannot be run as a program. |

The owner has Read and Write access (`rw-`), while group members and others only have Read access (`r--`).

---

### Task 3.4 — Explain operating-system responsibilities

| OS responsibility | Your explanation | Example |
| :--- | :--- | :--- |
| **Process management** | Makes sure multiple programs can run at the same time by sharing CPU time between them fairly. | Letting me listen to music on Spotify while typing code in VS Code without either app freezing. |
| **Memory management** | Decides which app gets how much RAM and frees up memory when an app is closed. | Giving 500 MB of RAM to Chrome when I open tabs, and giving that memory back when I close Chrome. |
| **Device management** | Communicates with connected hardware (like mouse, keyboard, printer) using device drivers. | Detecting when I plug in a USB mouse and translating mouse movements into the cursor moving on screen. |
| **File management** | Keeps all files and folders organized on the SSD, and keeps track of where data is stored. | Creating, saving, and organizing folders like `mission-00-setup` and files on my disk. |
| **User interface / shell** | Provides a way for humans to interact with the computer, either through desktop icons (GUI) or typed commands (CLI). | Clicking on app icons in the macOS Dock or typing commands in the zsh Terminal window. |
| **Security and permissions** | Protects system files and prevents unauthorized apps or users from changing important data. | Asking for my password/Touch ID before installing new software, and preventing standard apps from modifying system files. |

---

## 3. Commands / tools used
- `uname -srm`, `sw_vers` - Checked OS details and kernel version.
- `whoami` - Checked the active terminal user account.
- `df -h .` - Checked available and used disk storage space.
- `ps aux` - Looked at the list of running processes and their PIDs.
- `ls -l` - Inspected file permissions on practice files.

## 4. My understanding
Before this mission, I thought of an operating system just as the visual interface (like the desktop and menus). But now I understand that the OS does all the hard background work: it stops programs from crashing into each other's memory, schedules the CPU so multiple apps run smoothly, handles file storage, and makes sure one user cannot accidentally modify protected system files.

## 5. Difficulties faced
Reading the long table from `ps aux` was a bit overwhelming at first because hundreds of system processes were listed on the screen.

## 6. How I resolved them
I used `head -n 10` with a pipe (`ps aux | head -n 10`) to look at just the top few lines and read the column headers (`USER`, `PID`, `%CPU`, `COMMAND`) carefully to find specific apps like VS Code.

## 7. Evidence / files
- `mission-03-operating-system/README.md` with system inspection tables, process notes, and OS responsibilities.

## 8. Commit details
- Commit message: `Document operating system and file management`
- Pushed to: `main` branch on GitHub.
