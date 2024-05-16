message = input("Enter the message to encrypt/decrypt: ")
shift = int(input("Enter the shift value (an integer): "))

encrypted_message = ""
decrypted_message = ""

for char in message:
    if char.isalpha():
        shift_amount = shift % 26
        if char.islower():
            encrypted_char = chr(((ord(char) - ord('a') + shift_amount) % 26) + ord('a'))
            decrypted_char = chr(((ord(encrypted_char) - ord('a') - shift_amount) % 26) + ord('a'))
        else:
            encrypted_char = chr(((ord(char) - ord('A') + shift_amount) % 26) + ord('A'))
            decrypted_char = chr(((ord(encrypted_char) - ord('A') - shift_amount) % 26) + ord('A'))
    else:
        encrypted_char = char
        decrypted_char = char
    encrypted_message += encrypted_char
    decrypted_message += decrypted_char

print("Encrypted message:", encrypted_message)
print("Decrypted message:", decrypted_message)
