# ---------------------
# Shell sort algorithm.
# ---------------------

from random import randint                    # Importing randint item in random module.
n = 10                                        # Amount items in list.
a = [randint(0, n) for i in range(n)]         # Filling list of randoms numbers.
k = n // 2                                    # Searching middle position in list.
while k > 0:                                  # Passing through in list.
	for i in range(0, n - k):                 # Passing through in half list.
		j = i                                 # Copying i index to j variable.
		while (j >= 0) and (a[j] > a[j + k]): # Searching position for swap.
			a[j], a[j + k] = a[j + k], a[j]   # Swap a[j] and a[j + k].
			j -= 1                            # Decrement j for passing through in list.
	k = k // 2                                # Split list for next passing.