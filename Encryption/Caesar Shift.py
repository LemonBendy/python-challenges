from enchant import Dict

alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def encrypt(text, shift):
    encypted = ''
    for character in text:
        code = ord(character)
        if character in alphabet_lower:
            code += shift
            if code > ord('z'):
                code -= 26
            elif code < ord('a'):
                code += 26
        elif character in alphabet_upper:
            code += shift
            if code > ord('Z'):
                code -= 26
            elif code < ord('A'):
                code += 26
        encypted += chr(code)
    return encypted


def decrypt(text, shift):
    decypted = ''
    for character in text:
        code = ord(character)
        if character in alphabet_lower:
            code -= shift
            if code > ord('z'):
                code -= 26
            elif code < ord('a'):
                code += 26
        elif character in alphabet_upper:
            code -= shift
            if code > ord('Z'):
                code -= 26
            elif code < ord('A'):
                code += 26
        decypted += chr(code)
    return decypted


def brute_force(text):
    for i in range(26):
        text = decrypt(text, i)
        check = enchant.Dict("en_UK")
        if check.check(text):
            print("Decrypted text: ", text)
            print("Shift value: ", i)


def main():
    print("Would you like to encrypt or decrypt a message?")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Brute Force")
    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            text = input("Enter text to encrypt: ")
            shift = int(input("Enter shift value: "))
            encrypted = encrypt(text, shift)
            print("Encrypted text: ", encrypted)
            main()
        case 2:
            text = input("Enter text to decrypt: ")
            shift = int(input("Enter shift value: "))
            decrypted = decrypt(text, shift)
            print("Decrypted text: ", decrypted)
            main()
        case 3:
            text = input("Enter text to decrypt: ")
            brute_force(text)
            main()
        case _:
            print("Invalid choice")
            main()

main()
