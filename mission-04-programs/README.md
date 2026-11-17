# Mission 4 — How programs run

## 1. Task / objective
The goal of this mission was to write and run a simple one-line Python script (`hello.py`) from the Terminal using Python 3, and to understand how compilers and interpreters work when running computer programs.

## 2. Work completed

### Task 4.1 — Create and run a Python program
- Created a file named `hello.py` inside the `mission-04-programs/` directory.
- Added one line of Python code:
  ```python
  print("Hello from Python")
  ```
- Ran the program from Terminal using:
  ```bash
  python3 mission-04-programs/hello.py
  ```
- **Observed output**:
  ```
  Hello from Python
  ```

---

### Task 4.2 — Compare compiler and interpreter

| Point | Compiler | Interpreter |
| :--- | :--- | :--- |
| **When translation / execution happens** | Translates the whole program into machine code all at once **before** the program runs. | Translates and executes the program line by line **while** the program is running. |
| **Typical output** | Creates a separate runnable binary file (like an `.exe` file or binary executable). | Does not create a standalone binary file; it executes instructions directly in memory. |
| **One example** | **C** or **C++** (using `gcc` or `clang`), or **Rust** | **Python** (using Python 3), or **JavaScript** |
| **One advantage** | Runs much faster because the computer can directly execute the compiled machine code without translating it again. | Easier to write and test code because you can run your script immediately and fix errors right away without waiting to recompile. |

#### Difference between compiler and interpreter (in my own words):
A compiler takes your entire code and converts it into computer machine code all at once before you run it. This creates a ready-to-run executable file that runs very fast on your machine. On the other hand, an interpreter reads your program line by line and executes each line on the spot as it runs. Even though compiled programs run faster, interpreted languages like Python are great because you can test changes instantly and write code much quicker without worrying about a long compilation step every time you fix a bug.

---

## 3. Commands / tools used
- Text editor to create and edit `hello.py`.
- `python3 mission-04-programs/hello.py` in Terminal to execute the Python script.

## 4. My understanding
Computers only understand binary machine code (0s and 1s), so humans can't easily write software directly in machine language. High-level languages like Python or C let us write code that humans can understand, but that code needs to be translated into machine instructions. Understanding the difference between compiling ahead of time and interpreting on the fly helped me see why C/C++ is used for high-speed systems (like game engines or OS kernels) while Python is so popular for quick scripting, learning, and data work.

## 5. Difficulties faced
I wondered if Python is only an interpreter or if it compiles anything under the hood, because I sometimes see `__pycache__` folders.

## 6. How I resolved them
I found out that Python actually does a mix: it first compiles `.py` files into intermediate "bytecode" (which gets stored in `.pyc` files in `__pycache__`), and then the Python Virtual Machine interprets that bytecode line by line.

## 7. Evidence / files
- `mission-04-programs/hello.py` (working script).
- `mission-04-programs/README.md`.

## 8. Commit details
- Commit message: `Compare compilers and interpreters`
- Pushed to: `main` branch on GitHub.
