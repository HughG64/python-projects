# Write a function called caesar_cipher that:

# Takes a message and a shift number
# Shifts every letter forward by shift positions in the alphabet
# Leaves spaces and punctuation unchanged
# Returns the encoded message

# pythonprint(caesar_cipher("hello", 3))  # "khoor"
# print(caesar_cipher("abc", 1))    # "bcd"
# Hint — ord() converts a character to its ASCII number, chr() converts back. You'll need those. 🙂

def caesar_cipher(message, shift):
    result = ""
    for letter in message:
        if letter.isalpha():
            base = ord('A') if letter.isupper() else ord('a')
            result += chr((ord(letter) - base + shift) % 26 + base)
        else:
            result += letter

    return result

print(caesar_cipher("hello", 3))
print(caesar_cipher("abz", 1))
print(caesar_cipher("Hello", 3))
