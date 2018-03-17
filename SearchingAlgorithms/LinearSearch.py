# -----------------------
# Linear search algorithm.
# -----------------------

def linearsearch(a, x):
	for i in range(0, len(a)):   # Passing through in list.
		if a[i] == x:            # Searching index of number.
			return i             # Return result.
	return -1

def visualization():
	from random import randint                           # Importing randint item in random module.
	n = 10                                               # Choice random length of list.
	a = [randint(0, n) for i in range(0, n)]             # Filling list from 0 to n numbers.
	x = randint(0, n - 1)                                # Create random numbers for searching.
	print("Initial list:", a)                            # Printing initial list.
	print("The number of which must be found:", x)       # Printing searching number.
	r = linearsearch(a, x)                               # Searching number.
	if r != -1:                                          # If result there is then 
		print("Result of searching: ", r)                # - printing result,
	else:										         # Else then 
		print("This number does not exist in the list.") # - printing that result no exist.

import timeit
elapsed_time = timeit.timeit(visualization, number = 1) # Start program and counting elapsed time.
print("Elapsed time: ", round(elapsed_time, 3), "sec.") # Printing elapsed time.