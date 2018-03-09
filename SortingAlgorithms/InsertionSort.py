# ------------------------
# Insertion sort algorithm.
# ------------------------

from random import randint             # Importing randint item in random module.
n = 10                                 # Amount items in list.
a = [randint(0, n) for i in range(n)]  # Filling list of randoms numbers.
for i in range(0, n):                  # Passing through in list from 0 to n.
	x = a[i]                           # Assign value a[i] to x.
	j = i                              # Assign index i to j.
	while (j > 0) and (a[j - 1] > x):  # Searching insertion point.
		a[j] = a[j - 1]                # Swap a[j] and a[j - 1].
		j -= 1                         # Decrement j for passing through indexes.
	a[j] = x                           # Assign a[j] to x.