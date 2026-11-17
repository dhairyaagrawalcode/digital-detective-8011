# Mission 1 — Know your computer

## 1. Task / objective
The goal of Mission 1 is to understand the fundamental architecture of computer systems, specifically the IPOS cycle (Input, Processing, Output, Storage), classify essential computer hardware and software categories (system, application, and utility software), and analyze real-world embedded or computer-based systems encountered in everyday life.

---

## 2. Work completed

### Task 1.1 — Trace one activity using IPOS
**Activity Selected**: Typing and saving a programming script (e.g., creating a Python program in an editor).

| Stage | What happens in your example? | Possible hardware / component |
| :--- | :--- | :--- |
| **Input** | Keystrokes are pressed by the user. Each key switch generates an electrical signal translated into an ASCII/UTF-8 character code and sent to the computer controller via USB or internal bus. | Keyboard / Touchpad |
| **Processing** | The CPU receives interrupts from the keyboard, loads the character codes into main memory (RAM), calculates formatting, and renders the updated text buffer through the application logic. | CPU (Processor) and RAM (Memory) |
| **Output** | The graphics subsystem converts the text data from the display framebuffer into pixels, rendering the characters instantly on the monitor so the programmer can read what was typed. | Display / Monitor (Retina screen) |
| **Storage** | When the user triggers the Save command (`Cmd+S` / `Ctrl+S`), the operating system transfers the text buffer from volatile RAM across the storage bus to persistent non-volatile flash memory on the SSD. | Solid State Drive (SSD) / Flash Storage |

#### Data Flow Explanation
1. **Input to Processing**: When a key is tapped on the keyboard, hardware interrupts alert the operating system kernel. The keyboard controller translates physical key depressions into scan codes and stores them into an input queue in memory (RAM).
2. **Processing to Output**: The text editor application reads the scan codes from memory, updates its internal text buffer in RAM, and makes draw calls to the graphics rendering engine. The GPU processes these draw calls and writes the visual raster data to the display buffer, which refreshes the monitor screen at 60Hz/120Hz.
3. **Processing to Storage**: The in-memory buffer in RAM is volatile; turning off the computer would erase it. When the save operation is invoked, the OS file management subsystem allocates filesystem blocks on the SSD, writes the stream of bytes from RAM to flash blocks, and commits the file metadata (name, size, timestamp) to the drive.

---

### Task 1.2 — Identify hardware and software

| Item / Software Name | Hardware or Software? | Software Type (if applicable) | Purpose |
| :--- | :--- | :--- | :--- |
| **Mechanical Keyboard** | Hardware | Not applicable | Captures physical keypresses and inputs textual data and shortcut commands. |
| **Apple M-Series CPU/GPU** | Hardware | Not applicable | Executes computational instructions, manages registers, and processes graphics. |
| **Liquid Retina Display** | Hardware | Not applicable | Presents graphical user interface (GUI) and visual outputs to the user. |
| **NVMe SSD Storage** | Hardware | Not applicable | Provides persistent non-volatile long-term storage for the OS, apps, and documents. |
| **macOS** | Software | Operating system software | Manages system resources (CPU scheduling, memory, file system, hardware abstraction). |
| **Visual Studio Code** | Software | Application software | Integrated code editor providing syntax highlighting, file editing, and terminal integration. |
| **Google Chrome** | Software | Application software | Web browser used for internet browsing, researching documentation, and web app usage. |
| **Activity Monitor** | Software | Utility software | System utility that tracks CPU usage, RAM allocations, disk reads/writes, and process activity. |
| **Disk Utility** | Software | Utility software | Diagnoses disk integrity, manages storage partitions, and formats volumes. |

---

### Task 1.3 — Computer systems around you

| System | Main Purpose | One Input | One Output |
| :--- | :--- | :--- | :--- |
| **Automated Teller Machine (ATM)** | Enables self-service banking transactions, cash withdrawals, and account balance queries. | Numeric PIN keypad / EMV chip card reader | Physical cash dispenser / printed receipt slip / display screen |
| **Smart Traffic Signal Controller** | Automates traffic light sequences based on road congestion, pedestrian calls, and scheduled intervals. | Inductive road loop sensors / pedestrian crossing push-button | Traffic signal lamps (Red, Yellow, Green) / pedestrian countdown timer |
| **Smart Television** | Receives, decodes, and streams digital multimedia content and runs on-demand applications. | Infrared (IR) or Bluetooth remote control / built-in microphone for voice commands | 4K display panel / audio speaker system |
| **Metro Ticket Vending Machine (TVM)** | Issues transit cards/tokens and processes commuter fares automatically. | Touchscreen fare selection / currency bill & coin validator | Dispensed smart travel token / printed paper ticket |

---

## 3. Commands / tools used
- Text Editor (VS Code / Markdown editor): Used to draft and structure the observation tables.
- Terminal: Used to confirm system hardware architecture (`sysctl -n machdep.cpu.brand_string` / `uname -m`).
- Activity Monitor: Inspected as an example of built-in utility software managing background tasks.

---

## 4. My understanding
A computer is fundamentally an information transformation machine built upon the IPOS cycle:
- Without **Input**, the computer has no data to act upon.
- Without **Processing**, data cannot be organized, transformed, or evaluated.
- Without **Output**, results cannot be communicated or acted upon by human users or other machines.
- Without **Storage**, state is lost immediately when power is removed because RAM is volatile.

Software acts as the instruction layer that makes hardware purposeful. Operating systems form the foundation by arbitrating hardware access, application software fulfills specific end-user goals, and utility software preserves the health, security, and performance of the computing environment. Modern embedded systems like ATMs and smart traffic controllers demonstrate that computing principles extend far beyond traditional personal computers into ubiquitous physical infrastructure.

---

## 5. Difficulties faced
Distinguishing clearly between utility software and operating system software, as many modern utilities come bundled directly with the operating system (e.g., Disk Utility, Activity Monitor).

---

## 6. How I resolved them
Clarified the definition: the operating system is the core platform managing fundamental operations and resource allocation (kernel, device drivers, shell), whereas utility software consists of specialized maintenance tools that analyze, configure, optimize, or protect the system, regardless of whether they are bundled with the OS or installed separately.

---

## 7. Evidence / files
- `mission-01-computer-basics/README.md`: Completed IPOS, hardware/software, and everyday system tables.

---

## 8. Commit details
- Commit message: `Complete computer basics and IPOS mission`
- Status: Staged, committed, and pushed to `main` branch on GitHub.
