# -----------------------
# Cocktail sort algortihm.
# -----------------------

def cocktail(a, n):
	l, r = 0, n - 1                             # Create start and finish position.
	while l <= r:                               # Passing through in list.
		for i in range(l, r, +1):               # Passing through from start to finish.
			if a[i] > a[i + 1]:                 # If a[i] more a[i + 1] then
				a[i], a[i + 1] = a[i + 1], a[i] # - swap a[i] and a[i + 1].
		r -= 1                                  # Decrement r because value a last item the biggest.
		for i in range(r, l, -1):               # Passing through from finish to start.
			if a[i - 1] > a[i]:                 # If a[i - 1] more a[i] then
				a[i], a[i - 1] = a[i - 1], a[i] # - swap a[i] and a[i - 1].
		l += 1                                  # Increment l because value a first item the smallest.
		print(" ", [l], "-->", a)               # Printing sorting status.
	return a, l                                 # Return sorted list and number passages.

def visualization():
	from random import randint                  # Importing randint item in random module.
	n = 10                                      # Amount items in list.
	a = [randint(0, n) for i in range(n)]       # Filling list of randoms numbers.
	print("Initial list:", a)                   # Printing initial list.
	print("Visualization of algorithm work.")   # Printing decription.
	a, i = cocktail(a, n)                       # Sorting list.
	print("Final list:", a)                     # Printing final list.
	print("Total numbers of passages:", i)      # Printing numbers of passages.

import timeit
elapsed_time = timeit.timeit(visualization, number = 1) # Start program and counting elapsed time.
print("Elapsed time: ", round(elapsed_time, 3), "sec.") # Printing elapsed time.