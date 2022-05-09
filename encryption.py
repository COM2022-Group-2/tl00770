s=10

def encryp(MESSAGE):
    encryptedMsg = MESSAGE
   # transverse the plain text
    for i in range(len(MESSAGE)):
        char = MESSAGE[i]
        # Encrypt uppercase characters in plain text
        
        if (char.isupper()):
            encryptedMsg += chr((ord(char) + s-65) % 26 + 65)
        # Encrypt lowercase characters in plain text
        else:
            encryptedMsg += chr((ord(char) + s - 97) % 26 + 97)
        return encryptedMsg

    
def decrypt(MESSAGE):
    LETTERS = 'sfgadshjfgdjhadsjkgfjdgfkjasyukeyuhukdhguakg123'

    for key in range(len(LETTERS)):
        translated = ''
        for symbol in MESSAGE:
            if symbol in LETTERS:
                num = LETTERS.find(symbol)
                num = num - key
                if num < 0:
                    num = num + len(LETTERS)
                translated = translated + LETTERS[num]
            else:
                translated = translated + symbol
        return translated
