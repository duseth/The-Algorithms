def encryption():
	global textString, cipherText, wordKey
	textString, wordKey, cipherText = textString.upper(), wordKey.upper(), ""
	wordKey *= len(textString) // len(wordKey) + 1
	for index, symbol in enumerate(textString):
		if re.search('[A-Z]', symbol):
			temp = ord(symbol) + ord(wordKey[index])
			cipherText += chr(temp % 26 + ord('A'))
		else:
			cipherText += symbol

def decryption():
	global textString, cipherText, wordKey
	cipherText, wordKey, textString = cipherText.upper(), wordKey.upper(), ""
	wordKey *= len(cipherText) // len(wordKey) + 1
	for index, symbol in enumerate(cipherText):
		if re.search('[A-Z]', symbol):
			temp = ord(symbol) - ord(wordKey[index])
			textString += chr(temp % 26 + ord('A'))
		else:
			textString += symbol

def decryptionMode():
	global textString, cipherText, wordKey

	print("\n » Decryption mode activated! « (~˘▾˘)~")

	try:
		cipherText = str(input("[+] Enter your cipher text - "))
		checking = cipherText[0]
		wordKey = str(input("[+] Enter your key - "))
		checking = wordKey[0]
	except IndexError:
		print("[x] Invalid input! For example: \"hello\".")
		raise SystemExit

	decodingPerformance = "%.5f" % timeit.timeit(decryption, number = 1)

	print("\n »» The result of decryption by Vigenere algorithm. ««")
	print(textString)
	print("\n[~] Vigenere algorithm decoding performance - {} sec.".format(decodingPerformance))

def encryptionMode():
	global textString, cipherText, wordKey

	print("\n » Encryption mode activated! « (~˘▾˘)~")

	try:
		textString = str(input("[+] Enter your text - "))
		checking = textString[0]
		wordKey = str(input("[+] Enter your key - "))
		checking = wordKey[0]
	except IndexError:
		print("[x] Invalid input! For example: \"hello\".")
		raise SystemExit

	encodingPerformance = "%.5f" % timeit.timeit(encryption, number = 1)

	print("\n »» The result of encryption by Vigenere algorithm. ««")
	print(cipherText)
	print("\n[~] Vigenere algorithm encoding performance - {} sec.".format(encodingPerformance))

def main():
	print("\t\t[x] Vigenere cryptography algorithm. [x]")
	print(" • 0. Encryption mode.\n • 1. Decryption mode.")

	try:
		mode = int(input("[?] Select program mode - "))
	except:
		print("[x] Invalid input! For example: \"1, 2\".")
		raise SystemExit 
	if mode == 0:
		encryptionMode()
	elif mode == 1:
		decryptionMode()
	else:
		print("[x] Invalid input! You can only select: \"0, 1\".")
		raise SystemExit 

if __name__ == '__main__':
	textString, cipherText, wordKey = "", "", ""
	import timeit
	import random
	import re
	main()