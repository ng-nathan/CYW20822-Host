#!/usr/bin/env python3
import sys

def ascii_to_hex_counter(text):
    try:
        # Convert ASCII to hex only
        hex_values = text.encode('ascii').hex()
        # Count bytes (2 hex digits = 1 byte)
        byte_count = len(hex_values) // 2
        # Convert byte count to hex format (uppercase, no '0x' prefix)
        hex_bytes = f"{byte_count:02X}"
        
        return {
            'hex': hex_values,
            'byte_count': byte_count,
            'hex_byte_count': hex_bytes
        }
    except UnicodeEncodeError:
        print("Error: Input contains non-ASCII characters")
        sys.exit(1)

def main():
    # Check if input is provided as command line argument
    if len(sys.argv) > 1:
        text = sys.argv[1]
    else:
        # If no command line argument, prompt for input
        text = input("Enter ASCII text to convert: ")
    
    # Process the text
    result = ascii_to_hex_counter(text)
    
    # Print results
    print("\nResults:")
    print(f"Original text: {text}")
    print(f"Pure hex value: {result['hex']}")
    print(f"Byte count: {result['byte_count']}")
    print(f"Byte count in hex: {result['hex_byte_count']}")

if __name__ == "__main__":
    main()