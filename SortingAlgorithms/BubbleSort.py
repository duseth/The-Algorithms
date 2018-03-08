
# ---------------------
# Bubble sort algorithm.
# ---------------------

from random import randint                  # Importing randint item in random module.
n = 10                                      # Amount items in list
a = [randint(0, 10) for i in range(n)]      # Filling list of randoms numbers.
for i in range(0, n - 1):                   # Passing through the list (n - 1) times.
	f = 0                                   # Mark for break if list sorted.
	for j in range(0, n - 1):               # Passing through the list from 0 to (n - 1).
		if a[j] > a[j + 1]:                 # Comparison a[j] and a[j + 1].
			a[j], a[j + 1] = a[j + 1], a[j] # Swap items.
			f = 1                           # Mark for continued passing.
	if f == 0:                              # If list sorted -
		break                               # - break passing.