# Ilyas Salimov, 2018
# Implemented on Python 3.5.2
# My understanding of this algorithm.

def encryption():
	global textString, cipherText, key
	textString, key, cipherText = textString.upper(), str(key), ""
	key *= len(textString) // len(key) + 1
	for index, symbol in enumerate(textString):
		if re.search('[A-Z]', symbol):
			temp = ord(symbol) + int(key[index]) - 13
			cipherText += chr(temp % 26 + ord('A'))
		else:
			cipherText += symbol

def decryption():
	global textString, cipherText, key
	cipherText, key, textString = cipherText.upper(), str(key), ""
	key *= len(cipherText) // len(key) + 1
	for index, symbol in enumerate(cipherText):
		if re.search('[A-Z]', symbol):
			temp = ord(symbol) - int(key[index]) - 13
			textString += chr(temp % 26 + ord('A'))
		else:
			textString += symbol

def decryptionMode():
	global textString, cipherText, key
	print("\n » Decryption mode activated! « (~˘▾˘)~")
	try:
		cipherText = str(input("[+] Enter your cipher text - "))
		checking = cipherText[0]
		key = int(input("[+] Enter your key - "))
	except IndexError:
		print("[x] Invalid input! For example: \"hello\".")
		raise SystemExit 
	except ValueError:
		print("[x] Invalid input! For example: \"1, 2, 3\".")
		raise SystemExit 
	decodingPerformance = "%.5f" % timeit.timeit(decryption, number = 1)
	print("\n »» The result of decryption by Gronsfeld algorithm. ««")
	print(textString)
	print("\n[~] Gronsfeld algorithm decoding performance - {} sec.".format(decodingPerformance))

def encryptionMode():
	global textString, cipherText, key
	print("\n » Encryption mode activated! « (~˘▾˘)~")
	try:
		textString = str(input("[+] Enter your text - "))
		checking = textString[0]
		key = int(input("[+] Enter your key - "))
	except IndexError:
		print("[x] Invalid input! For example: \"hello\".")
		raise SystemExit 
	except ValueError:
		print("[x] Invalid input! For example: \"1, 2, 3\".")
		raise SystemExit 
	encodingPerformance = "%.5f" % timeit.timeit(encryption, number = 1)
	print("\n »» The result of encryption by Gronsfeld algorithm. ««")
	print(cipherText)
	print("\n[~] Gronsfeld algorithm encoding performance - {} sec.".format(encodingPerformance))

def main():
	print("\t\t[x] Gronsfeld cryptography algorithm. [x]")
	print(" • 0. Encryption mode.\n • 1. Decryption mode.")
	try:
		mode = int(input("[?] Select program mode - "))
	except:
		print("[x] Invalid input! For example: \"1, 2, 3\".")
		raise SystemExit 
	if mode == 0:
		encryptionMode()
	elif mode == 1:
		decryptionMode()
	else:
		print("[x] Invalid input! You can only select: \"0, 1\".")
		raise SystemExit 

textString, cipherText, key = "", "", 0
import timeit, random, re
main()