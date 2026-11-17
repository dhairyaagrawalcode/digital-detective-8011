# Mission 5 — Numbers and data

## 1. Task / objective
The objective of Mission 5 is to understand how computer hardware represents and processes data at the fundamental bit and byte level. This encompasses calculating number base conversions manually (decimal, binary, and hexadecimal), verifying calculation accuracy using Python 3 built-in conversion functions, engineering an interactive CLI utility (`number_converter.py`), and analyzing text character encodings (ASCII and UTF-8).

---

## 2. Work completed

### Task 5.1 — Convert numbers by hand

| Question | Step-by-Step Manual Working | Final Answer |
| :--- | :--- | :--- |
| **Convert decimal 13 to binary** | Repeated division by 2:<br>• $13 \div 2 = 6$, remainder **1** (LSB)<br>• $6 \div 2 = 3$, remainder **0**<br>• $3 \div 2 = 1$, remainder **1**<br>• $1 \div 2 = 0$, remainder **1** (MSB)<br>Read remainders bottom-to-top: | `1101₂` |
| **Convert decimal 25 to binary** | Repeated division by 2:<br>• $25 \div 2 = 12$, remainder **1** (LSB)<br>• $12 \div 2 = 6$, remainder **0**<br>• $6 \div 2 = 3$, remainder **0**<br>• $3 \div 2 = 1$, remainder **1**<br>• $1 \div 2 = 0$, remainder **1** (MSB)<br>Read remainders bottom-to-top: | `11001₂` |
| **Convert binary 1010 to decimal** | Positional expansion in base 2:<br>• $(1 \times 2^3) + (0 \times 2^2) + (1 \times 2^1) + (0 \times 2^0)$<br>• $= 8 + 0 + 2 + 0$ | `10₁₀` |
| **Convert binary 1101 to decimal** | Positional expansion in base 2:<br>• $(1 \times 2^3) + (1 \times 2^2) + (0 \times 2^1) + (1 \times 2^0)$<br>• $= 8 + 4 + 0 + 1$ | `13₁₀` |
| **Convert hexadecimal A to decimal** | Positional expansion in base 16:<br>• In hexadecimal, $A = 10$<br>• $(10 \times 16^0) = 10 \times 1$ | `10₁₀` |
| **Convert hexadecimal 1F to decimal** | Positional expansion in base 16:<br>• In hexadecimal, $F = 15$<br>• $(1 \times 16^1) + (15 \times 16^0)$<br>• $= 16 + 15$ | `31₁₀` |
| **Convert binary 1111 to hexadecimal** | Group 4 bits into base 16 digit:<br>• $(1 \times 2^3) + (1 \times 2^2) + (1 \times 2^1) + (1 \times 2^0) = 8 + 4 + 2 + 1 = 15_{10}$<br>• In hexadecimal, value 15 corresponds to digit $F$ | `F₁₆` (or `0xF`) |

---

### Task 5.2 — Verify using Python

| Target Conversion | Tested Python Expression | Python Result | Matches Manual Calculation? |
| :--- | :--- | :--- | :--- |
| Decimal 13 to binary | `bin(13)` | `'0b1101'` | Yes, matches `1101₂` |
| Decimal 25 to binary | `bin(25)` | `'0b11001'` | Yes, matches `11001₂` |
| Binary 1010 to decimal | `int("1010", 2)` | `10` | Yes, matches `10₁₀` |
| Binary 1101 to decimal | `int("1101", 2)` | `13` | Yes, matches `13₁₀` |
| Hexadecimal A to decimal | `int("A", 16)` | `10` | Yes, matches `10₁₀` |
| Hexadecimal 1F to decimal | `int("1F", 16)` | `31` | Yes, matches `31₁₀` |
| Binary 1111 to hexadecimal | `hex(0b1111)` | `'0xf'` | Yes, matches `F₁₆` |

---

### Task 5.3 — Build a small number converter
Developed the Python converter script `number_converter.py` inside `mission-05-numbers-data/`.
- Prompting user input via `input()`.
- Parsing string input safely into integer with error handling (`int(..., 10)`).
- Formatting binary with `bin()` and hexadecimal with `hex()`.

#### Test Execution Records

| Test Number (Decimal) | Binary Output (`bin()`) | Hexadecimal Output (`hex()`) |
| :--- | :--- | :--- |
| **13** | `0b1101` (Clean: `1101`) | `0xD` (Clean: `D`) |
| **25** | `0b11001` (Clean: `11001`) | `0x19` (Clean: `19`) |
| **255** | `0b11111111` (Clean: `11111111`) | `0xFF` (Clean: `FF`) |

#### Explanation of Python Conversion Functions
- `bin(x)`: Takes an integer $x$ and returns a string prefixed with `'0b'` representing the number in two's complement binary notation (base 2).
- `hex(x)`: Takes an integer $x$ and returns a lowercase string prefixed with `'0x'` representing the number in hexadecimal notation (base 16).
- `int(string, base)`: Converts a number represented in a given numeric string format back into an integer using the specified positional radix/base (e.g., base 2 for binary, base 16 for hexadecimal).

---

### Task 5.4 — How is text stored?

#### ASCII Decimal Code Findings
- Uppercase **'A'**: ASCII Decimal **65** (Binary: `01000001`, Hex: `0x41`)
- Lowercase **'a'**: ASCII Decimal **97** (Binary: `01100001`, Hex: `0x61`)
*(Verified via Python using `ord('A')` and `ord('a')`)*

#### Why Computers Need an Encoding Standard
Because digital electronic hardware can only store and manipulate binary state charges (0s and 1s), computers cannot physically understand human alphabets or typographic glyphs directly. An encoding standard establishes a universal, unambiguous mapping contract between numeric binary values and human characters, ensuring that a text document created on one machine is interpreted and displayed identically on any other system worldwide.

#### Character Outside Basic ASCII
- **Indian Rupee symbol (`₹`)**: Unicode code point `U+20B9`. Basic 7-bit ASCII only covers codes 0 through 127 (English alphabet, digits, and control characters); modern multi-byte standards like UTF-8 use 3 bytes (`0xE0 0xA4 0xB9`) to represent the Rupee symbol.

---

## 3. Commands / tools used
- Python 3 interactive shell: Verified mathematical conversions using `bin()`, `hex()`, `int()`, and `ord()`.
- `python3 mission-05-numbers-data/number_converter.py`: Executed and tested the interactive conversion script.
- Markdown editor: Documented the step-by-step arithmetic proofs.

---

## 4. My understanding
All digital computation is grounded in number representation. While humans use base 10 (decimal) due to historical ten-finger counting, digital circuits utilize binary (base 2) because two voltage states (on/off, high/low) are physically reliable and noise-tolerant. Hexadecimal (base 16) serves as a human-friendly shorthand for binary, where every 4 binary bits (a nibble) maps exactly to 1 hex digit. Character encoding bridges mathematical bit patterns and human language communication, progressing from 7-bit ASCII to modern universal UTF-8.

---

## 5. Difficulties faced
Handling negative numbers or invalid string inputs in the Python CLI script without causing the program to crash with an unhandled `ValueError`.

---

## 6. How I resolved them
Implemented Python `try-except` exception handling blocks around `int(user_input)` to intercept non-numeric characters gracefully and added input validation to ensure positive integers.

---

## 7. Evidence / files
- `mission-05-numbers-data/number_converter.py`: Working Python converter script.
- `mission-05-numbers-data/README.md`: Documented arithmetic derivations, Python verifications, and text-encoding analysis.

---

## 8. Commit details
- Commit message: `Build number converter and practise data representation`
- Status: Staged, committed, and pushed to `main` branch on GitHub.
