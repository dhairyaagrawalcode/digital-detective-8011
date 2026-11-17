"""
Digital Detective - Mission 5: Number Systems and Data
Interactive Number Converter
Converts a positive decimal integer into binary and hexadecimal representations.
"""

def main():
    print("=" * 45)
    print("     DIGITAL DETECTIVE - NUMBER CONVERTER    ")
    print("=" * 45)
    
    user_input = input("Enter a positive decimal integer: ").strip()
    
    try:
        decimal_val = int(user_input)
        if decimal_val < 0:
            print("Error: Please enter a positive integer.")
            return
            
        binary_str = bin(decimal_val)       # converts integer to binary format (with '0b' prefix)
        hex_str = hex(decimal_val)          # converts integer to hexadecimal format (with '0x' prefix)
        
        print("\n--- Conversion Results ---")
        print(f"Decimal Value     : {decimal_val}")
        print(f"Binary Format     : {binary_str} (Clean: {binary_str[2:]})")
        print(f"Hexadecimal Format: {hex_str.upper().replace('0X', '0x')} (Clean: {hex_str[2:].upper()})")
        print("-" * 45)
        
    except ValueError:
        print(f"Error: '{user_input}' is not a valid integer.")

if __name__ == "__main__":
    main()
