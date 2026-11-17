# Mission 5 — Numbers and data

## 1. Task / objective
The goal of this mission was to learn how computers represent numbers and text using binary bits. I practiced converting numbers between decimal, binary, and hexadecimal by hand, verified my math using Python built-in functions, built a Python script (`number_converter.py`) that converts user input, and explored character encodings like ASCII and UTF-8.

## 2. Work completed

### Task 5.1 — Convert numbers by hand

| Question | Your working and answer |
| :--- | :--- |
| **Convert decimal 13 to binary.** | Divide 13 by 2 repeatedly and keep track of remainders:<br>• 13 / 2 = 6 with remainder **1**<br>• 6 / 2 = 3 with remainder **0**<br>• 3 / 2 = 1 with remainder **1**<br>• 1 / 2 = 0 with remainder **1**<br>Reading remainders from bottom to top gives: **1101** in binary. |
| **Convert decimal 25 to binary.** | Divide 25 by 2 repeatedly and keep track of remainders:<br>• 25 / 2 = 12 with remainder **1**<br>• 12 / 2 = 6 with remainder **0**<br>• 6 / 2 = 3 with remainder **0**<br>• 3 / 2 = 1 with remainder **1**<br>• 1 / 2 = 0 with remainder **1**<br>Reading remainders from bottom to top gives: **11001** in binary. |
| **Convert binary 1010 to decimal.** | Multiply each bit by powers of 2 starting from the right (power 0):<br>• (1 * 2^3) + (0 * 2^2) + (1 * 2^1) + (0 * 2^0)<br>• = 8 + 0 + 2 + 0<br>• = **10** in decimal. |
| **Convert binary 1101 to decimal.** | Multiply each bit by powers of 2:<br>• (1 * 2^3) + (1 * 2^2) + (0 * 2^1) + (1 * 2^0)<br>• = 8 + 4 + 0 + 1<br>• = **13** in decimal. |
| **Convert hexadecimal A to decimal.** | In hexadecimal: 0–9 are digits, and A=10, B=11, C=12, D=13, E=14, F=15.<br>• A = 10 * 16^0 = **10** in decimal. |
| **Convert hexadecimal 1F to decimal.** | In hexadecimal, F represents 15.<br>• (1 * 16^1) + (15 * 16^0)<br>• = 16 + 15<br>• = **31** in decimal. |
| **Convert binary 1111 to hexadecimal.** | First convert binary 1111 to decimal:<br>• (1 * 2^3) + (1 * 2^2) + (1 * 2^1) + (1 * 2^0) = 8 + 4 + 2 + 1 = 15.<br>In hexadecimal, the number 15 is represented by the letter **F** (or **0xF**). |

---

### Task 5.2 — Verify using Python
I opened the terminal, ran `python3` to start the interactive prompt, and tested each conversion:

| Conversion tested | Expression tested | Python result | Matches manual calculation? |
| :--- | :--- | :--- | :--- |
| Decimal 13 to binary | `bin(13)` | `'0b1101'` | Yes, matches `1101` |
| Decimal 25 to binary | `bin(25)` | `'0b11001'` | Yes, matches `11001` |
| Binary 1010 to decimal | `int("1010", 2)` | `10` | Yes, matches `10` |
| Binary 1101 to decimal | `int("1101", 2)` | `13` | Yes, matches `13` |
| Hexadecimal A to decimal | `int("A", 16)` | `10` | Yes, matches `10` |
| Hexadecimal 1F to decimal | `int("1F", 16)` | `31` | Yes, matches `31` |
| Binary 1111 to hexadecimal | `hex(0b1111)` | `'0xf'` | Yes, matches `F` |

All Python results matched my manual step-by-step calculations.

---

### Task 5.3 — Build a small number converter
I created `number_converter.py` in this folder. It asks the user to enter a positive decimal number, converts it to binary using `bin()` and to hexadecimal using `hex()`, and prints both outputs.

#### Program test runs:

| Test number | Binary output | Hexadecimal output |
| :--- | :--- | :--- |
| **13** | `0b1101` (or `1101`) | `0xd` (or `D`) |
| **25** | `0b11001` (or `11001`) | `0x19` (or `19`) |
| **255** | `0b11111111` (or `11111111`) | `0xff` (or `FF`) |

#### What the binary and hexadecimal conversion functions do:
- `bin()` takes an integer number in Python and returns a string starting with `'0b'` showing that number in binary (base 2).
- `hex()` takes an integer number in Python and returns a string starting with `'0x'` showing that number in hexadecimal (base 16).

---

### Task 5.4 — How is text stored?

- **ASCII decimal codes for 'A' and 'a':**  
  - Uppercase **'A'** has an ASCII decimal value of **65**.
  - Lowercase **'a'** has an ASCII decimal value of **97**.  
  *(I tested this in Python using `ord('A')` and `ord('a')`)*.
- **Why does a computer need an encoding standard to store text?**  
  Computers can only store numbers made of electrical 1s and 0s; they cannot store letters or symbols directly. An encoding standard assigns a specific number to every letter and symbol so computers always know which character to show on the screen when reading saved bytes.
- **Example of a character not part of basic ASCII:**  
  The Indian Rupee symbol **`₹`** (or emoji like **`😊`**) is not part of basic 7-bit ASCII, which only goes from 0 to 127. Characters like this need modern standards like UTF-8 to be stored.

---

## 3. Commands / tools used
- Python 3 interactive shell to test functions like `bin()`, `hex()`, `int()`, and `ord()`.
- `python3 mission-05-numbers-data/number_converter.py` to test the script with numbers `13`, `25`, and `255`.

## 4. My understanding
Everything inside a computer—numbers, code, images, and text—is made of bits (0s and 1s). Decimal uses base 10 because humans have ten fingers, but electronics work best with base 2 (switches are either on or off). Hexadecimal (base 16) is really convenient because exactly 4 binary bits make 1 hexadecimal character, making long binary strings much easier to read. Understanding ASCII and UTF-8 also explained why files sometimes get garbled if opened with the wrong text encoding.

## 5. Difficulties faced
When writing the converter, if the user typed text or letters instead of numbers, Python threw a `ValueError`.

## 6. How I resolved them
I used `user_input.isdigit()` in the Python script to check whether the input consists of numbers before converting it with `int()`. If the user types anything invalid, the script displays a helpful message instead of crashing.

## 7. Evidence / files
- `mission-05-numbers-data/number_converter.py` (working script).
- `mission-05-numbers-data/README.md`.

## 8. Commit details
- Commit message: `Build number converter and practise data representation`
- Pushed to: `main` branch on GitHub.
