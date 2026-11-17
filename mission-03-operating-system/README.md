# Mission 3 — Understand the operating system

## 1. Task / objective
The objective of Mission 3 is to examine the core components and duties of the operating system (OS). This involves exploring the OS runtime environment, identifying current account context and storage utilization, analyzing active processes and Process Identifiers (PIDs), distinguishing between absolute and relative file paths, examining Unix file permission modes (`r`, `w`, `x`), and detailing the key operational responsibilities of modern operating systems.

---

## 2. Work completed

### Task 3.1 — Explore your operating system

| Information Explored | What it tells you | Your Observation (privacy-safe) |
| :--- | :--- | :--- |
| **Operating system / system details** (`uname -srm`, `sw_vers`) | Identifies the OS name, kernel release version, and hardware processor architecture. | macOS (Darwin Kernel 27.2.0, ARM64 Apple Silicon architecture) |
| **Current account identity** (`whoami`, `id`) | Reveals the username and user ID (UID) of the currently logged-in interactive shell account. | Active user: `[redacted]` (UID: `501`, primary group: `staff`) |
| **Available and used storage** (`df -h .`) | Displays filesystem capacity, disk space consumed, available free space, and mount points in human-readable units. | Filesystem: `/System/Volumes/Data`<br>Total: `926 GiB`<br>Used: `210 GiB` (24%)<br>Available: `692 GiB` |
| **System activity snapshot** (`ps aux`, `top -l 1`) | Captures a point-in-time snapshot of active processes, CPU/memory consumption, state, and runtime. | Active CPU load moderate; top active tasks include user desktop apps (VS Code, Browser) and system daemons (`WindowServer`, `opendirectoryd`). |

---

### Task 3.2 — Understand processes

#### Conceptual Questions
- **What is a process?**  
  A process is an active instance of a computer program currently being executed by the operating system. While a program stored on disk is passive code and data, a process is dynamic: it possesses its own address space in memory, execution threads, program counter, registers, open file descriptors, and allocated system resources.
- **What does the PID column represent?**  
  PID stands for **Process Identifier**. It is a unique numeric integer assigned by the operating system kernel to identify and track each running process during its lifetime. The OS kernel, user utilities, and system calls use the PID to signal, monitor, prioritize, or terminate (`kill`) processes.
- **Two examples of processes running on the computer:**
  1. **User Application Process**: Visual Studio Code / Web Browser (PID e.g. `10318`) — an interactive GUI application running in user space.
  2. **System Background Daemon**: `WindowServer` (PID e.g. `404`) — a macOS system daemon responsible for compositing windows, rendering visual elements to displays, and handling system-level display events.

---

### Task 3.3 — Understand paths and permissions

#### Absolute Paths vs. Relative Paths
- **Absolute Path**: Specifies the exact, unambiguous location of a file or directory starting from the root of the filesystem (`/`). It is independent of the current working directory.
  - *Example from assignment*: `/Users/[redacted]/Documents/Projects/digital-detective-8011/terminal-practice/note.txt`
- **Relative Path**: Specifies a location relative to the shell's current working directory (`pwd`), using shorthand symbols like `.` (current directory) and `..` (parent directory).
  - *Example from assignment*: `./terminal-practice/note.txt` or `../digital-detective-8011`

#### File Permissions Analysis
Inspected file: `terminal-practice/note.txt`  
Command: `ls -l terminal-practice/note.txt`  
Output: `-rw-r--r--  1 [redacted]  staff  70  note.txt`

| Permission Bit | Meaning | Owner Rights on `note.txt` |
| :--- | :--- | :--- |
| **`r` (Read)** | Allows reading and viewing the file contents. | **Granted**: Owner can view and open the file. |
| **`w` (Write)** | Allows modifying, appending, or overwriting file contents. | **Granted**: Owner can edit and save changes. |
| **`x` (Execute)** | Allows running the file as a program or binary script (or entering a folder). | **Denied**: Owner cannot execute the file as a binary/script. |

- **Summary**: The owner has Read and Write permissions (`rw-`), the group has Read-only (`r--`), and other users have Read-only (`r--`).

---

### Task 3.4 — Explain operating-system responsibilities

| OS Responsibility | Your Explanation | Real-World Example |
| :--- | :--- | :--- |
| **Process Management** | Controls process creation, CPU scheduling (allocating processor time slices across multiple threads), process synchronization, and termination. | Switching execution between an active code editor, background music playback, and terminal commands seamlessly without freezing. |
| **Memory Management** | Allocates, tracks, and deallocates portions of physical RAM to processes; provides virtual memory and paging to prevent programs from overwriting each other's memory. | Allocating 400 MB of RAM when opening a web browser and releasing that memory block back to the OS pool when the tab is closed. |
| **Device Management** | Interfaces with hardware peripherals through standardized device drivers, translating generic software requests into hardware-specific control signals. | Receiving input packets from a USB/Bluetooth keyboard or sending raster lines to a printer via a print spooler. |
| **File Management** | Organizes data into structured files and hierarchical directories on storage drives, handling allocation tables, read/write caching, and file metadata. | Reading and writing file data to APFS or ext4 storage blocks when saving `note.txt`. |
| **User Interface / Shell** | Provides an interface (Graphical User Interface like macOS Aqua or Command-Line Interface like zsh/bash) for humans to interact with system services. | Accepting typed commands like `ls` or `pwd` in the zsh Terminal or double-clicking an application icon on the desktop. |
| **Security and Permissions** | Enforces access control policies, authenticates users, isolates process memory spaces, and restricts unauthorized read/write/execute operations on protected system resources. | Preventing a normal user process from modifying system files in `/System` or executing privileged kernel extensions without explicit administrator authorization. |

---

## 3. Commands / tools used
- `uname -srm`: Identified operating system kernel name, release, and hardware architecture.
- `sw_vers`: Inspected macOS product name and build version.
- `whoami` & `id`: Verified active user account and group identity.
- `df -h .`: Inspected disk volume usage and remaining capacity.
- `ps aux`: Inspected process table, PIDs, and resource utilization.
- `ls -l`: Inspected file permission bits, ownership, and links.

---

## 4. My understanding
The operating system acts as the master coordinator between physical computer hardware and user applications. Without an OS, every software application would need to implement its own device drivers, memory allocators, and hardware timers. By abstracting hardware behind system calls, enforcing process isolation through virtual memory, and safeguarding file permissions, the OS ensures system stability, multitasking concurrency, and security.

---

## 5. Difficulties faced
Understanding how processes share CPU cores concurrently even when there are more running threads than physical hardware cores.

---

## 6. How I resolved them
Researched OS CPU scheduling and time-slicing (preemptive multitasking): the kernel rapidly switches the CPU between threads using timer interrupts, giving each process small execution slices so they appear to run simultaneously.

---

## 7. Evidence / files
- `mission-03-operating-system/README.md`: Complete OS investigation tables, process analysis, path/permission breakdowns, and OS responsibility explanations.

---

## 8. Commit details
- Commit message: `Document operating system and file management`
- Status: Staged, committed, and pushed to `main` branch on GitHub.
