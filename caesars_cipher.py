def caesar_cipher_encrypt(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - 65 + key) % 26 + 65)
            else:
                result += chr((ord(char) - 97 + key) % 26 + 97)
        else:
            result += char
    return result

def caesar_cipher_decrypt(ciphertext, key):
    return caesar_cipher_encrypt(ciphertext, -key)

# Example usage
plaintext = "Hello, World!"
shift_key = 3

# Encrypt the plaintext
encrypted_text = caesar_cipher_encrypt(plaintext, shift_key)
print("Encrypted:", encrypted_text)

# Decrypt the ciphertext
decrypted_text = caesar_cipher_decrypt(encrypted_text, shift_key)
print("Decrypted:", decrypted_text)
