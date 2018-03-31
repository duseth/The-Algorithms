# =============================
# The main logic of the program.
# =============================

def prime(n):
	"""Function for checking number prime or not."""
	from math import sqrt # Importing sqrt item from math module.
	i = 2                 # Creating divider.
	while i <= sqrt(n):   # Passing through from i to sqrt(n).
		if n % i == 0:    # If (n mod i == 0) |=> (n is prime) then 
			return False  # - return False and stopping passing.
		i += 1            # Increment i for passing.
	return True           # Return True |=> (n not is prime).

def creation_keys():
	"""Function for creating open and close keys."""
	from random import randint                       # Importing randint item from random module.
	p, q, e = 10, 10, 4                              # Creating p, q, e variables and assigment not prime value.
	while not prime(p):                              # Finding prime value for p.
		p = randint(500, 700)                        # Assigment p to random integer value for finding.
	while not prime(q):                              # Finding prime value for q.
		q = randint(500, 700)                        # Assigment q to random integer value for finding.
	n, f, d = p * q, (p - 1) * (q - 1), 0            # Finding n, f, and creating d integer variable for passing through.
	while (not prime(e)) or (e > f) or (f % e == 0): # Finding e such that: (e is prime) or (e less f) or (f was not divisble e). 
		e += 1                                       # Increment i for passing.
	while (d * e) % f != 1:                          # Fingind d such thah: (d * e) mod f == 1.
		d += 1                                       # Increment d for passing.
	return (e, n), (d, n)                            # Return open and close keys.

def encoding():
	"""Functionn for encoding text with RSA algorithm."""
	global text, open_key, cipher_list
	cipher_list = []                             # Creating cipher_list list for encoded chars.
	e, n = open_key                              # Unpacking open_key tuple in e and n variables.
	for letter in text:                          # Passing through from text.
		cipher_list.append(ord(letter) ** e % n) # Append encoded char in cipher_list.

def decoding():
	"""Functionn for decoding text with RSA algorithm."""
	global cipher_list, close_key, text
	text = ""                           # Creating text string variable for decoded chars.
	d, n = close_key                    # Unpacking close_key tuple in d and n variables.
	for item in cipher_list:            # Passing through from cipher_list.
		text += chr(int(item) ** d % n) # Concatenation decoded char to text.

# ============================
# User and program interaction.
# ============================

def demonstration_mode():
	global text, open_key, close_key, cipher_list
	import timeit
	print("\n » Demonstration mode activated! « ¯\_(ツ)_/¯")
	try:
		text = str(input("[+] Enter your text - "))
		check = text[0]
	except:
		print("[x] Invalid input!")
		raise SystemExit
	open_key, close_key = creation_keys()
	print("[~] Your open key - [{},{}].".format(open_key[0], open_key[1]))
	print("[~] Your close key - [{},{}].".format(close_key[0], close_key[1]))
	encoding_performance = "%.5f" % timeit.timeit(encoding, number = 1)
	print("\n »» The result of encoding by RSA algorithm. ««")
	print(cipher_list)
	text = ""
	decoding_performance = "%.5f" % timeit.timeit(decoding, number = 1)
	print("\n »» The result of decoding by RSA algorithm. ««")
	print(text)
	print("\n[~] RSA algorithm encoding performance - {} sec.".format(encoding_performance))
	print("[~] RSA algorithm decoding performance - {} sec.".format(decoding_performance))

def encoding_mode():
	global text, open_key, cipher_list
	import timeit
	print("\n » Encoding mode activated! « (｡◕‿◕｡)")
	try:
		text = str(input("[+] Enter your text - "))
		check = text[0]
	except:
		print("[x] Invalid input!")
		raise SystemExit
	print(" • 0. Random open key.\n • 1. Your open key(for experienced).")
	key = int(input("[?] Select open key method - "))
	if key == 0:
		open_key, close_key = creation_keys()
		print("[~] Your open key - [{},{}].".format(open_key[0], open_key[1]))
		print("[~] Your close key - [{},{}].".format(close_key[0], close_key[1]))
	elif key == 1:
		open_key = tuple(map(int, str(input("[+] Enter your open key - ")).split(",")))
	encoding_performance = "%.5f" % timeit.timeit(encoding, number = 1)
	print("\n »» The result of encoding by RSA algorithm. ««")
	print(cipher_list)
	print("\n[~] RSA algorithm encoding performance - {} sec.".format(encoding_performance))

def decoding_mode():
	global text, close_key, cipher_list
	import timeit
	print("\n » Decoding mode activated! « (~˘▾˘)~")
	try:
		cipher_list = input("[+] Enter your cipher list - ")
		cipher_list = list(map(int, cipher_list[1:len(cipher_list) - 1].split(",")))
	except:
		print("[x] Invalid input!")
		raise SystemExit
	close_key = tuple(map(int, str(input("[+] Enter your close key - ")).split(",")))
	decoding_performance = "%.5f" % timeit.timeit(decoding, number = 1)
	print("\n »» The result of decoding by RSA algorithm. ««")
	print(text)
	print("\n[~] RSA algorithm decoding performance - {} sec.".format(decoding_performance))

def menu():
	print("\t\t✖ Rivest–Shamir–Adleman cryptography algorithm. ✖")
	print(" • 0. Demonstration mode.\n • 1. Encoding mode.\n • 2. Decoding mode.")
	try:
		id = int(input("[?] Select program mode - "))
	except:
		print("[x] Invalid input!")
		raise SystemExit
	if id == 0:
		demonstration_mode()
	elif id == 1:
		encoding_mode()
	elif id == 2:
		decoding_mode()

open_key, close_key, text, cipher_list = (), (), "", []
menu()