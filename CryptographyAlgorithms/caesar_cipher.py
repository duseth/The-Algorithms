def processing(text, key, mode):
	finished_text = ""
	for i in range(len(text)):
		if text[i].isalnum():
			if text[i].isupper():
				finished_text += chr((ord(text[i]) + key * mode - 65) % 26 + 65)
			else:
				finished_text += chr((ord(text[i]) + key * mode - 97) % 26 + 97)
		else:
			finished_text += text[i]

	return finished_text


def assembly(mode):
	text = str(input("[+] Enter your cipher text - "))
	key = int(input("[+] Enter your key - "))

	finished_text = processing(text, key, mode)

	print("\n »» The result of decryption by Caesar-Cipher algorithm. ««")
	print(finished_text)


def main():
	print("[x] Caesar-Cipher cryptography algorithm. [x]")
	print(" • 0. Encryption mode.\n • 1. Decryption mode.")

	mode = (-1) ** int(input("[?] Select program mode - "))
	assembly(mode)


if __name__ == '__main__':
	main()
