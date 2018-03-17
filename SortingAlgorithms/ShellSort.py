# ---------------------
# Shell sort algorithm.
# ---------------------

def shellsort(a, n):
	k, r = n // 2, 0                              # Searching middle position in list.
	while k > 0:                                  # Passing through in list.
		for i in range(0, n - k):                 # Passing through in half list.
			j = i                                 # Copying i index to j variable.
			while (j >= 0) and (a[j] > a[j + k]): # Searching position for swap.
				a[j], a[j + k] = a[j + k], a[j]   # Swap a[j] and a[j + k].
				j, r = j - 1, r + 1               # Decrement j for passing through in list and increment r.
				print(" ", [r], "-->", a)         # Printing sorting status.
		k = k // 2                                # Split list for next passing.
	return a, r                                   # Return sorted list and number passages.

def visualization():
	from random import randint                  # Importing randint item in random module.
	n = 10                                      # Amount items in list.
	a = [randint(0, n) for i in range(n)]       # Filling list of randoms numbers.
	print("Initial list:", a)                   # Printing initial list.
	print("Visualization of algorithm work.")   # Printing decription.
	a, i = shellsort(a, n)                      # Sorting list.
	print("Final list:", a)                     # Printing final list.
	print("Total numbers of passages:", i)      # Printing numbers of passages.

import timeit
elapsed_time = timeit.timeit(visualization, number = 1) # Start program and counting elapsed time.
print("Elapsed time: ", round(elapsed_time, 3), "sec.") # Printing elapsed time.