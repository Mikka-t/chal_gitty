def caesar_cipher():

    input_text = input("Enter the text to rotate: ")
    n = int(input("Enter the value of n: "))
    n = n % 26

    result = ""

    for char in input_text:
        if char.islower():
            result += chr((ord(char) - 97 + n) % 26 + 97)
        elif char.isupper():
            result += chr((ord(char) - 65 + n) % 26 + 65)
        else:
            result += char
    return result