# Ilyas Salimov, 2018
# Implemented on Python 3.5.2
# My understanding of this algorithm.

def encryption():
	global textString, cipherText, key
	textString, cipherText = textString.upper(), ""
	for symbol in textString:
		if re.search('[A-Z]', symbol):
			cipherText += chr((ord(symbol) + key - 13) % 26 + ord('A'))
		else:
			cipherText += symbol

def decryption():
	global textString, cipherText, key
	cipherText, textString = cipherText.upper(), ""
	for symbol in cipherText:
		if re.search('[A-Z]', symbol):
			textString += chr((ord(symbol) - key - 13) % 26 + ord('A'))
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
	print("\n »» The result of decryption by Caesar-Cipher algorithm. ««")
	print(textString)
	print("\n[~] Caesar-Cipher algorithm decoding performance - {} sec.".format(decodingPerformance))

def encryptionMode():
	global textString, cipherText, key
	print("\n » Encryption mode activated! « (~˘▾˘)~")
	try:
		textString = str(input("[+] Enter your text - "))
		checking = textString[0]
		print(" • 0. Your key.\n • 1. Random key.")
		keyMode = int(input("[?] Select key mode - "))
		if keyMode == 0:
			key = int(input("[+] Enter your key - "))
		elif keyMode == 1:
			key = random.randint(1, 25)
			print("[~] Your key - {}".format(key))
		else:
			print("[x] Invalid input! For example: \"0, 1\".")
			raise SystemExit 
	except IndexError:
		print("[x] Invalid input! For example: \"hello\".")
		raise SystemExit 
	except ValueError:
		print("[x] Invalid input! For example: \"1, 2, 3\".")
		raise SystemExit 
	encodingPerformance = "%.5f" % timeit.timeit(encryption, number = 1)
	print("\n »» The result of encryption by Caesar-Cipher algorithm. ««")
	print(cipherText)
	print("\n[~] Caesar-Cipher algorithm encoding performance - {} sec.".format(encodingPerformance))

def main():
	print("\t\t[x] Caesar-Cipher cryptography algorithm. [x]")
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