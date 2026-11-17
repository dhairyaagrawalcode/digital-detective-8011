# Mission 5 - Number Converter
# Student: Dhairya Agrawal (2402608011)

def convert_number():
    print("--- Number Converter ---")
    user_input = input("Enter a positive decimal number: ").strip()
    
    # Check if the input is a valid positive integer
    if not user_input.isdigit():
        print("Error: Please enter a positive whole number.")
        return
    
    num = int(user_input)
    
    # Convert using Python's built-in functions
    bin_output = bin(num)
    hex_output = hex(num)
    
    print("\nResults:")
    print("Decimal    :", num)
    print("Binary     :", bin_output, f"(without prefix: {bin_output[2:]})")
    print("Hexadecimal:", hex_output, f"(without prefix: {hex_output[2:].upper()})")

if __name__ == "__main__":
    convert_number()
