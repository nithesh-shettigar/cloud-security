import math

def encryptMessage(msg, key):
	cipher = ""
	k_indx = 0
	msg_len = float(len(msg))
	msg_lst = list(msg)
	key_lst = sorted(list(key))
	col = len(key)
	row = int(math.ceil(msg_len / col))
	fill_null = int((row * col) - msg_len)
	msg_lst.extend('_' * fill_null)
	matrix = [msg_lst[i: i + col] for i in range(0, len(msg_lst), col)]

	for _ in range(col):
		curr_idx = key.index(key_lst[k_indx])
		cipher += ''.join([row[curr_idx] for row in matrix])
		k_indx += 1

	return cipher
    
msg = input ("Enter the message to be encrypted: ")
key = input ("Enter the key for encryption: ")
cipher1 = encryptMessage(msg, key)
print(f"\nSingle Transpotion Cipher of message '{msg}' with key '{key}':\t", cipher1)
cipher2 = encryptMessage(cipher1, key)
print(f"\nDouble transposed message '{msg}' with key '{key}' is\n\t'",cipher2,"'")

# Decryption
def decryptMessage(cipher2):
	msg = ""

	k_indx = 0

	msg_indx = 0
	msg_len = float(len(cipher2))
	msg_lst = list(cipher2)
	col = len(key)
	row = int(math.ceil(msg_len / col))
	key_lst = sorted(list(key))
	dec_cipher = []
	for _ in range(row):
		dec_cipher += [[None] * col]

	for _ in range(col):
		curr_idx = key.index(key_lst[k_indx])

		for j in range(row):
			dec_cipher[j][curr_idx] = msg_lst[msg_indx]
			msg_indx += 1
		k_indx += 1


	try:
		msg = ''.join(sum(dec_cipher, []))
	except TypeError:
		raise TypeError("This program cannot handle repeating words.")

	null_count = msg.count('_')

	if null_count > 0:
		return msg[: -null_count]

	return msg

plain1=decryptMessage(cipher2)
print(plain1)
plain2=decryptMessage(plain1)
print(plain2)