def onetimepadding(text, key):
    result = ""
    if len(text) == len(key):
        for char, char1 in zip(text, key):
            if char.isalpha() and char1.isalpha():
                if char.isupper():
                    result += chr((ord(char) + ord(char1) - 2 * ord('A')) % 26 + ord('A'))
                else:
                    result += chr((ord(char) + ord(char1) - 2 * ord('a')) % 26 + ord('a'))
            else:
                # If either the plaintext or the key contains non-alphabetic characters,
                # simply append the original character without encryption.
                result += char
    else:
        print("Error: The length of the text and key must be the same.")

    return result

# Example usage
plaintext = "IOT"
key = "XYZ"

# Encrypt the plaintext
encrypted_text = onetimepadding(plaintext, key)
print("Encrypted:", encrypted_text)

# Decrypt the ciphertext
decrypted_text = onetimepadding(encrypted_text, key)
print("Decrypted:", decrypted_text)
