def codesTable(char):
	table = {
	"A":11, "B":21, "C":31, "D":41, "E":51,
	"F":12, "G":22, "H":32, "I":42, "K":52,
	"L":13, "M":23, "N":33, "O":43, "P":53,
	"Q":14, "R":24, "S":34, "T":44, "U":54,
	"V":15, "W":25, "X":35, "Y":45, "Z":55, "J":0,

	11:"A", 21:"B", 31:"C", 41:"D", 51:"E",
	12:"F", 22:"G", 32:"H", 42:"I", 52:"K",
	13:"L", 23:"M", 33:"N", 43:"O", 53:"P",
	14:"Q", 24:"R", 34:"S", 44:"T", 54:"U",
	15:"V", 25:"W", 35:"X", 45:"Y", 55:"Z", 0:"J"
	}
	return table[char] 

def encoding():
	global textString, cipherText
	textString, cipherText = textString.upper(), ""
	for symbol in textString:
		if re.search('[A-Z]', symbol):
			cipherText += str(codesTable(symbol)) + " "

def decoding():
	global textString, cipherText
	cipherText, textString = cipherText.upper(), ""
	for symbol in list(map(int, cipherText.split())):
		textString += codesTable(symbol)

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
	print("\n »» The result of decoding by Polybius Square algorithm. ««")
	print(textString)
	print("\n[~] Polybius Square algorithm decoding performance - {} sec.".format(decodingPerformance))

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
	print("\n »» The result of encoding by Polybius Square algorithm. ««")
	print(cipherText)
	print("\n[~] Polybius Square algorithm encoding performance - {} sec.".format(encodingPerformance))

def main():
	print("\t\t[x] Polybius Square cryptography algorithm. [x]")
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
	import timeit, random, re
	main()