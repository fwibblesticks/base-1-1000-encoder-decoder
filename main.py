def create_base_chars(base):
    chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    if base <= len(chars):
        return chars[:base]
    
    # Extended chars if base is bigger than 62
    extended_chars = list(chars)
    for i in range(len(chars), base):
        extended_chars.append(chr(i + 128))
    return ''.join(extended_chars)

def encode_base_n(text, base):
    if base == 1:
        # Special case for base-1 (unary)
        return '1' * sum(ord(c) for c in text)
    
    decimal = 0
    for char in text:
        decimal = decimal * 256 + ord(char)
    
    if decimal == 0:
        return '0'
    
    # Convert decimal to desired base
    base_chars = create_base_chars(base)
    result = ''
    while decimal > 0:
        decimal, remainder = divmod(decimal, base)
        result = base_chars[remainder] + result
    
    return result

def decode_base_n(encoded_text, base):
    if base == 1:
        # Special case for base-1 (unary)
        if not all(c == '1' for c in encoded_text):
            return "Invalid base-1 encoding"
        decimal = len(encoded_text)
        return chr(decimal)
    
    base_chars = create_base_chars(base)
    # Create reverse lookup dictionary
    char_to_val = {char: val for val, char in enumerate(base_chars)}
    
    decimal = 0
    for char in encoded_text:
        if char not in char_to_val:
            return "Invalid character in input"
        decimal = decimal * base + char_to_val[char]
    
    # Convert decimal to ASCII string
    result = ''
    while decimal > 0:
        decimal, remainder = divmod(decimal, 256)
        result = chr(remainder) + result
    
    return result

def main():
    while True:
        print("\nBase-N Encoder/Decoder")
        print("1. Encode")
        print("2. Decode")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == '3':
            break
        
        if choice not in ['1', '2']:
            print("Invalid choice. Please try again.")
            continue
        
        try:
            base = int(input("Enter the base (1-1000): "))
            if not 1 <= base <= 1000:
                print("Base must be between 1 and 1000")
                continue
                
            if choice == '1':
                text = input("Enter text to encode: ")
                result = encode_base_n(text, base)
                print(f"Encoded (Base-{base}): {result}")
            else:
                encoded_text = input(f"Enter Base-{base} text to decode: ")
                result = decode_base_n(encoded_text, base)
                print(f"Decoded: {result}")
                
        except ValueError as e:
            print(f"Error: {e}")
            continue

if __name__ == "__main__":
    main()
