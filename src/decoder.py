#!/usr/bin/env python3
import sys

def hex_to_ascii_decoder(hex_string):
    try:
        # Validate hex string length (must be even)
        if len(hex_string) % 2 != 0:
            raise ValueError("Invalid hex string length - must be even")
        
        # Convert hex to ASCII
        ascii_text = bytes.fromhex(hex_string).decode('ascii')
        byte_count = len(hex_string) // 2
        
        return {
            'ascii_text': ascii_text,
            'original_hex': hex_string,
            'byte_count': byte_count
        }
        
    except ValueError as e:
        print(f"Error: {str(e)}")
        sys.exit(1)
    except UnicodeDecodeError:
        print("Error: Invalid hex values or non-ASCII characters in encoded data")
        sys.exit(1)

def main():
    # Check if input is provided as command line argument
    if len(sys.argv) > 1:
        hex_input = sys.argv[1]
    else:
        # If no command line argument, prompt for input
        hex_input = input("Enter hex string to decode: ")
    
    # Remove any spaces or '0x' prefix if present
    hex_input = hex_input.replace(' ', '').replace('0x', '')
    
    # Process the hex string
    result = hex_to_ascii_decoder(hex_input)
    
    # Print results
    print("\nResults:")
    print(f"Original hex: {result['original_hex']}")
    print(f"Decoded ASCII text: {result['ascii_text']}")
    print(f"Byte count: {result['byte_count']}")

if __name__ == "__main__":
    main()