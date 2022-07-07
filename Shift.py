def ShiftEncrypt(text,key):
	cipher =""
	for i in range(len(text)):
		char=text[i]
		if char.isupper():
			cipher += chr((ord(char)+key-65)%26+65)

		else:
			cipher += chr((ord(char)+key-97)%26+97)
	return cipher
def ShiftDecrypt(cipher,key):
	plain =""
	for i in range(len(cipher)):
		char=cipher[i]
		if char.isupper():
			plain += chr((ord(char)-key-65)%26+65)

		else:
			plain += chr((ord(char)-key-97)%26+97)
	return plain


msg=input("enter the Message to encrypt")
key=int(input("Enter the key"))

cipher_text=ShiftEncrypt(msg,key)
print(cipher_text)

plain_text=ShiftDecrypt(cipher_text,key)
print(plain_text)