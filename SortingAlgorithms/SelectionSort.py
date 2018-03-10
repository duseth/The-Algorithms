# ------------------------
# Selection sort algorithm.
# ------------------------

from random import randint            # Importing randint item in random module.
n = 10                                # Amount items in list.
a = [randint(0, n) for i in range(n)] # Filling list of randoms numbers.
for i in range(0, n - 1):             # Passing through in list.
	l = i                             # Create a new variable with i value.
	for j in range(i + 1, n):         # Passing through in list that searching smalles value.
		if a[j] < a[l]:               # If a[j] less a[l] then
			l = j                     # - assign l to j
	a[i], a[l] = a[l], a[i]           # Swap a[i] and a[j].