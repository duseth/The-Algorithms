def codesTable(char):
	table = {
	"A":".-", "B":"-...", "C":"-.-.", "D":"-..", "E":".",
	"F":"..-.", "G":"--.", "H":"....", "I":"..", "J":".---", 
	"K":"-.-", "L":".-..", "M":"--", "N":"-.", "O":"---", 
	"P":".--.",	"Q":"--.-", "R":".-.", "S":"...", "T":"-", 
	"U":"..-", "V":"...-", "W":".--", "X":"-..-", "Y":"-.--", "Z":"--..",

	".-":"A", "-...":"B", "-.-.":"C", "-..":"D", ".":"E",
	"..-.":"F", "--.":"G", "....":"H", "..":"I", ".---":"J",
	"-.-":"K", ".-..":"L", "--":"M", "-.":"N", "---":"O", 
	".--.":"P", "--.-":"Q", ".-.":"R", "...":"S", "-":"T", 
	"..-":"U", "...-":"V", ".--":"W", "-..-":"X", "-.--":"Y", "--..":"Z",

	"0":"-----", "1":".----", "2":"..---", "3":"...--", "4":"....-",
	"5":".....", "6":"-....", "7":"--...", "8":"---..", "9":"----.",

	"-----":"0", ".----":"1", "..---":"2", "...--":"3", "....-":"4",
	".....":"5", "-....":"6", "--...":"7", "---..":"8", "----.":"9"
	}

	return table[char]

def encoding():
	global textString, cipherText
	textString, cipherText = textString.upper(), ""
	for symbol in textString:
		if not re.search('[A-Z0-9]', symbol):
			textString = textString.replace(symbol, "")
	for symbol in textString:
		cipherText += codesTable(symbol) + " "

def decoding():
	global textString, cipherText
	cipherText, textString = cipherText.upper(), ""
	for code in cipherText.split():
		textString += codesTable(code)

def decodingMode():
	global textString, cipherText, wordKey

	print("\n » Decoding mode activated! « (~˘▾˘)~")

	try:
		cipherText = str(input("[+] Enter your cipher text - "))
		checking = cipherText[0]
	except IndexError:
		print("[x] Invalid input! For example: \"hello\".")
		raise SystemExit

	decodingPerformance = "%.5f" % timeit.timeit(decoding, number = 1)

	print("\n »» The result of decoding by Morse algorithm. ««")
	print(textString)
	print("\n[~] Morse algorithm decoding performance - {} sec.".format(decodingPerformance))

def encodingMode():
	global textString, cipherText, wordKey

	print("\n » Encoding mode activated! « (~˘▾˘)~")

	try:
		textString = str(input("[+] Enter your text - "))
		checking = textString[0]
	except IndexError:
		print("[x] Invalid input! For example: \"hello\".")
		raise SystemExit

	encodingPerformance = "%.5f" % timeit.timeit(encoding, number = 1)

	print("\n »» The result of encoding by Morse algorithm. ««")
	print(cipherText)
	print("\n[~] Morse algorithm encoding performance - {} sec.".format(encodingPerformance))

def main():
	print("\t\t[x] Morse cryptography algorithm. [x]")
	print(" • 0. Encoding mode.\n • 1. Decoding mode.")

	try:
		mode = int(input("[?] Select program mode - "))
	except:
		print("[x] Invalid input! For example: \"1, 2\".")
		raise SystemExit 
	if mode == 0:
		encodingMode()
	elif mode == 1:
		decodingMode()
	else:
		print("[x] Invalid input! You can only select: \"0, 1\".")
		raise SystemExit 

if __name__ == '__main__':
	textString, cipherText = "", ""
	import timeit
	import random
	import re
	main()