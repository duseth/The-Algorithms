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
	global text, open_key, cipher_list           # Identify global variables.
	cipher_list = []                             # Creating cipher_list list for encoded chars.
	e, n = open_key                              # Unpacking open_key tuple in e and n variables.
	for letter in text:                          # Passing through from text.
		cipher_list.append(ord(letter) ** e % n) # Append encoded char in cipher_list.

def decoding():
	"""Function for decoding text with RSA algorithm."""
	global cipher_list, close_key, text # Identify global variables.
	text = ""                           # Creating text string variable for decoded chars.
	d, n = close_key                    # Unpacking close_key tuple in d and n variables.
	for item in cipher_list:            # Passing through from cipher_list.
		text += chr(int(item) ** d % n) # Concatenation decoded char to text.

# ============================
# User and program interaction.
# ============================

def demonstration_mode():
	"""Function for working demonstration mode."""
	global text, open_key, close_key, cipher_list                                            # Identify global variables.
	import timeit                                                                            # Importing timeit module.
	print("\n » Demonstration mode activated! « (~˘▾˘)~")                                    # Pringing header.
	try:                                                                                     # Exception construction start.
		text = str(input("[+] Enter your text - "))                                          # Input text.
		check = text[0]                                                                      # Checking for emptiness.
	except:                                                                                  # Exception handling.
		print("[x] Invalid input! For example: \"hello\".")                                  # Printing information to user.
		raise SystemExit                                                                     # Exit program.
	open_key, close_key = creation_keys()                                                    # Creating open and close keys.
	print("[~] Your open key - [{},{}].".format(open_key[0], open_key[1]))                   # Printing open key.
	print("[~] Your close key - [{},{}].".format(close_key[0], close_key[1]))                # Printing close key.
	encoding_performance = "%.5f" % timeit.timeit(encoding, number = 1)                      # Counting encoding elapse time.
	print("\n »» The result of encoding by RSA algorithm. ««")                               # Printing encoding result header.
	print(cipher_list)                                                                       # Printing encoding result.
	text = ""                                                                                # Cleaning text variable.
	decoding_performance = "%.5f" % timeit.timeit(decoding, number = 1)                      # Counting decoding elapse time.
	print("\n »» The result of decoding by RSA algorithm. ««")                               # Printung decoding result header.
	print(text)                                                                              # Printing decoding result.
	print("\n[~] RSA algorithm encoding performance - {} sec.".format(encoding_performance)) # Printing encoding performance.
	print("[~] RSA algorithm decoding performance - {} sec.".format(decoding_performance))   # Printing decoding performance.

def encoding_mode():
	"""Function for working encoding mode."""
	global text, open_key, cipher_list                                                       # Identify global variables.
	import timeit                                                                            # Importing timeit module.
	print("\n » Encoding mode activated! « (~˘▾˘)~")                                         # Printing header.
	try:                                                                                     # Exception construction start.
		text = str(input("[+] Enter your text - "))                                          # Input text.
		check = text[0]                                                                      # Checking for emptiness.
	except:                                                                                  # Exception handling.
		print("[x] Invalid input! For example: \"hello\".")                                  # Printing information to user.
		raise SystemExit                                                                     # Exit program.
	print(" • 0. Random open key.\n • 1. Your open key(for experienced).")                   # Print selection menu.
	key = int(input("[?] Select open key method - "))                                        # Input user choice.
	if key == 0:                                                                             # If user choiced random key then 
		open_key, close_key = creation_keys()                                                # - creating open and close keys,
		print("[~] Your open key - [{},{}].".format(open_key[0], open_key[1]))               # - printing open key,
		print("[~] Your close key - [{},{}].".format(close_key[0], close_key[1]))            # - printing close key.
	elif key == 1:                                                                           # Else if user choiced his key then
		open_key = tuple(map(int, str(input("[+] Enter your open key - ")).split(",")))      # - input user open key.
	encoding_performance = "%.5f" % timeit.timeit(encoding, number = 1)                      # Counting encoding elapse time.
	print("\n »» The result of encoding by RSA algorithm. ««")                               # Printing encoding result header.
	print(cipher_list)                                                                       # Printing encoding result.
	print("\n[~] RSA algorithm encoding performance - {} sec.".format(encoding_performance)) # Printing encoding performance.

def decoding_mode():
	"""Function for working decoding mode."""
	global text, close_key, cipher_list                                                      # Identify global variables.
	import timeit                                                                            # Importing timeit module.
	print("\n » Decoding mode activated! « (~˘▾˘)~")                                         # Printing header.
	try:                                                                                     # Exception construction start.
		cipher_list = input("[+] Enter your cipher list - ")                                 # Input string.
		if cipher_list[0] == "[":                                                            # Checking on extra signs.
			cipher_list = list(map(int, cipher_list[1:len(cipher_list) - 1].split(",")))     # Creating list of string and passing through for use int() for every item.
		else:                                                                                # Condition processing.
			cipher_list = list(map(int, cipher_list.split(",")))                             # Creating list of string and passing through for use int() for every item.
	except:                                                                                  # Exception handling.
		print("[x] Invalid input! For example: \"[1, 2, 3, 4, 5]\".")                        # Printing information to user.
		raise SystemExit                                                                     # Exit program.
	close_key = input("[+] Enter your close key - ")                                         # Input close key.
	if close_key[0] == "[":                                                                  # Checking on extra signs.
		close_key = tuple(map(int, close_key[1: len(close_key) - 1].split(",")))             # Input user close key.
	else:                                                                                    # Condition processing.
		close_key = tuple(map(int, close_key.split(",")))                                    # Input user close key.
	decoding_performance = "%.5f" % timeit.timeit(decoding, number = 1)                      # Counting decoding elapse time.
	print("\n »» The result of decoding by RSA algorithm. ««")                               # Printing decoding result header.
	print(text)                                                                              # Printing decoding result.
	print("\n[~] RSA algorithm decoding performance - {} sec.".format(decoding_performance)) # Printing decoding performance.

def menu():
	print("\t\t[x] Rivest–Shamir–Adleman cryptography algorithm. [x]")             # Printing header.
	print(" • 0. Demonstration mode.\n • 1. Encoding mode.\n • 2. Decoding mode.") # Print selection menu.
	try:                                                                           # Exception construction start.
		id = int(input("[?] Select program mode - "))                              # Input user choice.
	except:                                                                        # Exception handling.
		print("[x] Invalid input! For example: \"0, 1, 2\".")                      # Printing information to user.
		raise SystemExit                                                           # Exit program.
	if id == 0:                                                                    # If user choiced demonstation mode then
		demonstration_mode()                                                       # - calling demonstration_mode().
	elif id == 1:                                                                  # Else if user choiced encoding mode then
		encoding_mode()                                                            # - calling encoding_mode().
	elif id == 2:                                                                  # Else if user choiced decoding mode then 
		decoding_mode()                                                            # - calling decoding_mode().
	else:                                                                          # Else then 
		print("[x] Invalid input! You can only select: \"0, 1, 2\".")              # - printing information to user.
		raise SystemExit                                                           # - exit program.

open_key, close_key, text, cipher_list = (), (), "", [] # Creating global variables.
menu()                                                  # Starting program.