#Rot 13

# Encryption
# Cipher text, C = (P + K) mod 26
# C --> Cipher text
# P --> Plain text
# K --> key 
def encrypt(text, key):
    
    cipher_text = ""
    for i in range (len(text)):
        char = text[i] # getting each character of text for encryption

        # Encrypting uppercase characters 
        # here, the value of key is added to the order of character
        # and is subtacted and added by 65 (uppercase ASCII starts from 65)
        if char.isupper(): 
            cipher_text += chr((ord(char) + key - 65) % 26 + 65)
        
        # Encrypting lowercase characters
        # lower case ASCII starts from 97
        else:
            cipher_text += chr((ord(char) + key - 97) % 26 + 97)
    
    return cipher_text

# Decryption
# Plain text, P = (C - K) mod 26
# C --> Cipher text
# P --> Plain text
# K --> key 
def decrypt(cipher_text, key):
    
    plain_text = ""
    for i in range (len(cipher_text)):
        char = cipher_text[i] # getting each character of text for decryption

        # Decrypting uppercase characters 
        if char.isupper(): 
            plain_text += chr((ord(char) - key - 65) % 26 + 65)
        
        # Decrypting lowercase characters
        else:
            plain_text += chr((ord(char) - key - 97) % 26 + 97)
    
    return plain_text

msg= input('Enter a message to encrypt') 
key= int(input('Enter to key for encryption'))
cipher = encrypt(msg, key)
print(cipher)
plainText = decrypt(cipher, key) 
print(plainText)