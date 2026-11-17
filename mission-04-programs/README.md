# Mission 4 — How programs run

## 1. Task / objective
The objective of Mission 4 is to explore how computer programming languages execute instructions. This involves creating and running a Python script (`hello.py`) from the Terminal using the Python 3 interpreter, and analyzing the fundamental architectural differences between compilers and interpreters.

---

## 2. Work completed

### Task 4.1 — Create and run a Python program
- Created a Python script named `hello.py` inside the `mission-04-programs/` directory with the following content:
  ```python
  print("Hello from Python")
  ```
- Executed the program from the Terminal command line:
  ```bash
  python3 mission-04-programs/hello.py
  ```
- **Observed Terminal Output**:
  ```
  Hello from Python
  ```

---

### Task 4.2 — Compare compiler and interpreter

| Point | Compiler | Interpreter |
| :--- | :--- | :--- |
| **When translation / execution happens** | The entire source code is analyzed, optimized, and translated into target machine code **before runtime** during a distinct compilation build phase. Execution occurs separately later. | Source code or intermediate bytecode is translated and executed **dynamically at runtime**, instruction-by-instruction or statement-by-statement. |
| **Typical output** | Produces a permanent, standalone binary machine code file (e.g., `.exe`, ELF, Mach-O binary) ready to run on the CPU architecture. | Directly executes the program logic in memory; does not output a permanent standalone machine code binary. |
| **One example** | **C / C++** (compiled via `clang` / `gcc`), Rust, Go | **Python** (CPython runtime), JavaScript, Ruby |
| **One advantage** | **Superior execution speed and optimization**, because CPU instructions run directly on bare hardware with zero translation overhead during execution. | **Rapid iterative development and cross-platform flexibility**, allowing developers to test code immediately without repeating compile-link cycles. |

#### Detailed Comparison Explanation
A compiler translates the complete high-level source code into low-level machine code or binary instructions all at once before the program is executed, allowing the operating system and CPU to run it with maximum performance and optimization. In contrast, an interpreter parses, translates, and carries out program instructions incrementally at runtime, executing statements on the fly. While compiled programs run significantly faster and can catch many structural syntax and type errors during compilation, interpreted languages allow immediate code testing, intuitive interactive debugging, and write-once run-anywhere portability across different operating systems. Notably, modern language runtimes like Python often utilize a hybrid approach: Python source code is first compiled into bytecode (`.pyc`), which is then interpreted by the Python Virtual Machine (PVM).

---

## 3. Commands / tools used
- `touch mission-04-programs/hello.py`: Created the Python source script.
- `cat << 'EOF' > ...`: Wrote the Python print statement to the script.
- `python3 mission-04-programs/hello.py`: Invoked the Python 3 interpreter binary to execute the script.
- Markdown editor: Formatted the comparison tables and documentation.

---

## 4. My understanding
Computers cannot natively execute English-like human programming languages; the CPU understands only binary machine language (opcodes and operands). Compilers and interpreters bridge this semantic gap through two distinct execution philosophies. Compilers perform heavy lifting up front to produce lean, fast executables, whereas interpreters prioritize developer agility and dynamic runtime execution. Seeing `python3 hello.py` execute instantly demonstrates how the Python runtime transparently parses the source text, generates intermediate bytecode, and evaluates it on the host machine.

---

## 5. Difficulties faced
Understanding whether Python is purely an interpreted language or if it also involves compilation.

---

## 6. How I resolved them
Researched CPython's execution model: verified that Python actually compiles source code (`.py`) into bytecode (`.pyc` files stored in `__pycache__`), which is subsequently interpreted by the Python Virtual Machine, illustrating how modern languages blend compilation and interpretation.

---

## 7. Evidence / files
- `mission-04-programs/hello.py`: Verified working Python script.
- `mission-04-programs/README.md`: Complete compiler vs. interpreter documentation and execution logs.

---

## 8. Commit details
- Commit message: `Compare compilers and interpreters`
- Status: Staged, committed, and pushed to `main` branch on GitHub.
