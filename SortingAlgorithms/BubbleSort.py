# ---------------------
# Bubble sort algorithm.
# ---------------------

def bubblesort(a, n):
	for i in range(0, n - 1):                   # Passing through in list (n - 1) times.
		f = 0                                   # Mark for break if list sorted.
		for j in range(0, n - 1):               # Passing through in list from 0 to (n - 1).
			if a[j] > a[j + 1]:                 # Comparison a[j] and a[j + 1].
				a[j], a[j + 1] = a[j + 1], a[j] # Swap items.
				f = 1                           # Mark for continued passing.
		print(" ", [i + 1], "-->", a)           # Printing sorting status.
		if f == 0:                              # If list sorted then
			break                               # - break passing.
	return a, i + 1                             # Return sorted list and number passages.

def visualization():
	from random import randint                  # Importing randint item in random module.
	n = 10                                      # Amount items in list.
	a = [randint(0, n) for i in range(n)]       # Filling list of randoms numbers.
	print("Initial list:", a)                   # Printing initial list.
	print("Visualization of algorithm work.")   # Printing decription.
	a, i = bubblesort(a, n)                     # Sorting list.
	print("Final list:", a)                     # Printing final list.
	print("Total numbers of passages:", i)      # Printing numbers of passages.

import timeit
elapsed_time = timeit.timeit(visualization, number = 1) # Start program and counting elapsed time.
print("Elapsed time: ", round(elapsed_time, 3), "sec.") # Printing elapsed time.