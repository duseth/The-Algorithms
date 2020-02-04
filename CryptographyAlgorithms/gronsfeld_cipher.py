from string import ascii_uppercase as alphabet


def processing(text, key, mode):
	key *= len(text) // len(key) + 1
	text = text.upper()

	return ''.join([alphabet[alphabet.find(j) + int(key[i]) * mode] for i, j in enumerate(text)])


def assembly(mode):
	text = str(input("[+] Enter your text - "))
	key = str(input("[+] Enter your key - "))

	finished_text = processing(text, key, mode)

	print("\n »» The result of encryption by Gronsfeld cryptography algorithm. ««")
	print(finished_text)


def main():
	print("[x] Gronsfeld cryptography algorithm. [x]")
	print(" • 0. Encryption mode.\n • 1. Decryption mode.")

	mode = (-1) ** int(input("[?] Select program mode - "))

	assembly(mode)


if __name__ == '__main__':
	main()
