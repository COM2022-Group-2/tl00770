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
