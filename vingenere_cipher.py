def vigenere_cipher(plaintext, key, mode='encrypt'):
    def shift_char(char, shift):
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            return chr((ord(char) - base + shift) % 26 + base)
        else:
            return char

    key = key.lower()
    result = ""
    key_index = 0

    for char in plaintext:
        shift = ord(key[key_index]) - ord('a')
        if mode == 'encrypt':
            result += shift_char(char, shift)
        elif mode == 'decrypt':
            result += shift_char(char, -shift)
        else:
            raise ValueError("Invalid mode. Use 'encrypt' or 'decrypt'.")

        if char.isalpha():
            key_index = (key_index + 1) % len(key)

    return result

# Example usage:
plaintext = "Hello, World!"
key = "KEY"

# Encryption
encrypted_text = vigenere_cipher(plaintext, key, mode='encrypt')
print("Encrypted:", encrypted_text)

# Decryption
decrypted_text = vigenere_cipher(encrypted_text, key, mode='decrypt')
print("Decrypted:", decrypted_text)
