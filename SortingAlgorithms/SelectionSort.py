# ------------------------
# Selection sort algorithm.
# ------------------------

def selectionsort(a, n):
	for i in range(0, n - 1):             # Passing through in list.
		l = i                             # Create a new variable with i value.
		for j in range(i + 1, n):         # Passing through in list that searching smalles value.
			if a[j] < a[l]:               # If a[j] less a[l] then
				l = j                     # - assign l to j
		a[i], a[l] = a[l], a[i]           # Swap a[i] and a[j].
		print(" ", [i + 1], "-->", a)     # Printing sorting status.
	return a, i + 1                       # Return sorted list and number passages.

def visualization():
	from random import randint                  # Importing randint item in random module.
	n = 10                                      # Amount items in list.
	a = [randint(0, n) for i in range(n)]       # Filling list of randoms numbers.
	print("Initial list:", a)                   # Printing initial list.
	print("Visualization of algorithm work.")   # Printing decription.
	a, i = selectionsort(a, n)                  # Sorting list.
	print("Final list:", a)                     # Printing final list.
	print("Total numbers of passages:", i)      # Printing numbers of passages.

import timeit
elapsed_time = timeit.timeit(visualization, number = 1) # Start program and counting elapsed time.
print("Elapsed time: ", round(elapsed_time, 3), "sec.") # Printing elapsed time.