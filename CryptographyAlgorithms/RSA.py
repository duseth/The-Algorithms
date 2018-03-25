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

def encoding(text, open_key):
	"""Functionn for encoding text with RSA algorithm."""
	cipher_list = []                             # Creating cipher_list list for encoded chars.
	e, n = open_key                              # Unpacking open_key tuple in e and n variables.
	for letter in text:                          # Passing through from text.
		cipher_list.append(ord(letter) ** e % n) # Append encoded char in cipher_list.
	return cipher_list                           # Return encoded text as list.

def decoding(cipher_list, close_key):
	"""Functionn for decoding text with RSA algorithm."""
	text = ""                           # Creating text string variable for decoded chars.
	d, n = close_key                    # Unpacking close_key tuple in d and n variables.
	for item in cipher_list:            # Passing through from cipher_list.
		text += chr(int(item) ** d % n) # Concatenation decoded char to text.
	return text                         # Return decoded text.

# ============================
# User and program interaction.
# ============================

def user_input():
	"""Function to take text from the user and create keys."""
	try:                                                                         # Creating exception constructor.
		text = str(input("[+] Enter your text for encoding: "))                  # Input user text.
		check = text[0]                                                          # Checking for an empty variable.
	except:                                                                      # Exception handling.
		print("[x] Incorrect input!")                                            # Printing about empty variable.
		raise SystemExit                                                         # Exit from program.
	open_key, close_key = creation_keys()                                        # Unpacking the tuples returned by the function.
	print("  [!] Your open key: [{},{}].".format(open_key[0], open_key[1]))      # Printing open key.
	print("  [!] Your close key: [{},{}].\n".format(close_key[0], close_key[1])) # Printing close key.
	return text, open_key, close_key                                             # Return user data.

def run_encode():
	"""Function for run encoding."""
	global cipher_list, text, open_key               # Identify global variables.
	print(" RSA algorithm encoding result showing.") # Printing heading.
	print("»" + "—" * 60 + "»")                      # Creating top border.
	cipher_list = encoding(text, open_key)           # Encoding text with open key.
	i = 0                                            # Creating variable for control amount cols in row.
	for item in cipher_list:                         # Passing through in cipher_list list.
		if i == 7:                                   # Checking amount cols in row.
			i = 0                                    # Resetting a variable.
			print("\n")                              # Going to the next line.
		print(" " + "%-8s" % item, end = "")         # Printing item value within 8 tabs.
		i += 1                                       # Increment i for passing.
	print("\n", end = "")                            # Going to the next line.
	print("»" + "—" * 60 + "»")                      # Creating bottom border.

def run_decode():
	"""Function for run decoding."""
	global cipher_list, close_key                      # Identify global variables.
	print("\n RSA algorithm decoding result showing.") # Printing heading.
	text = decoding(cipher_list, close_key)            # Decoding cipher list with close key.
	print("«" + "—" * 60 + "«")                        # Creating top border.
	print(" ", end = "")                               # Creating tabulation in beginning line.
	i = 0                                              # Creating variable for control amount letters in line.
	for letter in text:                                # Passing through in text.
		if i == 60:                                    # Checking amount letters in line.
			print("\n")                                # Going to the next line.
			print(" ", end = "")                       # Creating tabulation in beginning line.
		print(letter, end = "")                        # Printing letter.
		i += 1                                         # Increment i for passing.
	print("\n", end = "")                              # Going to the next line.
	print("«" + "—" * 60 + "«\n")                      # Creating bottom border.

def performance():
	"""Function for counting and printing performance."""
	from timeit import timeit                                             # Importing timeit item from timeit module.
	elapsed_time_encode = "%.5f" % timeit(run_encode, number = 1)         # Counting time spent on encoding.
	elapsed_time_decode = "%.5f" % timeit(run_decode, number = 1)         # Counting time spent on decoding.
	print(" RSA algorithm performance statistics.")                       # Printing heading.
	print("»" + "—" * 60 + "»")                                           # Creating top border.
	print(" Time spent on encoding: {} sec.".format(elapsed_time_encode)) # Printing time spent on encoding.
	print(" Time spent on decoding: {} sec.".format(elapsed_time_decode)) # Printing time spent on decoding.
	print("»" + "—" * 60 + "»\n")                                         # Creating bottom border.

print("\t\tRivest–Shamir–Adleman cryptography algorithm.") # Printing heading.
text, open_key, close_key = user_input()                   # Unpacking user input in global variables.
cipher_list = []                                           # Creating cipher_list list for cipher values.
performance()                                              # Calling performance function and starting algorithm.