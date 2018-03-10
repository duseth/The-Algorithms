# -----------------------
# Linear search algorithm.
# -----------------------

from random import randint   # Importing randint item in random module.
n = randint(0, 25)           # Choice random length of list.
a = [i for i in range(0, n)] # Filling list from 0 to n numbers.
x, r = randint(0, n), 0      # Create random numbers for searching and result variable.
for i in range(0, n):        # Passing through in list.
	if a[i] == x:            # Searching index of number.
		r = i                # Write index in result variable.