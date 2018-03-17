# ------------------------
# Insertion sort algorithm.
# ------------------------

def insertionsort(a, n):
	for i in range(0, n):                  # Passing through in list from 0 to n.
		x = a[i]                           # Assign value a[i] to x.
		j = i                              # Assign index i to j.
		while (j > 0) and (a[j - 1] > x):  # Searching insertion point.
			a[j] = a[j - 1]                # Swap a[j] and a[j - 1].
			j -= 1                         # Decrement j for passing through indexes.
		a[j] = x                           # Assign a[j] to x.
		print(" ", [i + 1], "-->", a)      # Printing sorting status.
	return a, i + 1                        # Return sorted list and number passages.

def visualization():
	from random import randint                  # Importing randint item in random module.
	n = 10                                      # Amount items in list.
	a = [randint(0, n) for i in range(n)]       # Filling list of randoms numbers.
	print("Initial list:", a)                   # Printing initial list.
	print("Visualization of algorithm work.")   # Printing decription.
	a, i = insertionsort(a, n)                  # Sorting list.
	print("Final list:", a)                     # Printing final list.
	print("Total numbers of passages:", i)      # Printing numbers of passages.

import timeit
elapsed_time = timeit.timeit(visualization, number = 1) # Start program and counting elapsed time.
print("Elapsed time: ", round(elapsed_time, 3), "sec.") # Printing elapsed time.