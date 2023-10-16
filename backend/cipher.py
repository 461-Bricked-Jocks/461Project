def encrypt (string, N , D):
    string = string[::-1]
    encrypted = ""
    ascii = ''
    for char in string:
        ascii = ord(char) - 34
        if char == ' ' or char == '!':
            encrypted += char
            continue
        if D == 1:
            ascii += N
            ascii = ascii % (127-34)
            ascii += 34
        else:
            ascii -= N
            ascii = ascii % (127-34)
            ascii += 34
        encrypted += chr(ascii)    
    return encrypted
def decrypt(string, N, D):
    string = string[::-1]
    decrypted = ""
    ascii = ''
    for char in string:
        ascii = ord(char) - 34
        if char == ' ' or char == '!':
            decrypted += char
            continue
        if D == -1:
            ascii += N
            ascii = ascii % (127-34)
            ascii += 34
        else:
            ascii -= N
            ascii = ascii % (127-34)
            ascii += 34
        decrypted += chr(ascii)    
    return decrypted
