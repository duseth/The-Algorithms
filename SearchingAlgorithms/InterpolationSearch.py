# ------------------------------
# Interpolation search algorithm.
# ------------------------------

def interpolationsearch(a, x):
	l, h, r = 0, len(a) - 1, 1                          # Finding start and finish position.
	while (a[l] <= x) and (a[h] >= x):                  # Passing through in list.
		m = l + ((x - a[l]) * (h - l)) // (a[h] - a[l]) # Finding middle position in list.
		if a[m] < x:                                    # If a[m] less x then 
			l = m + 1                                   # - assign l to (m + 1), 
			print(" ", [r], "-->", a[l:])               # Printing searching status.
		elif a[m] > x:                                  # Else if a[m] more x then 
			h = m - 1                                   # - assign h to (m - 1), 
			print(" ", [r], "-->", a[:h])               # Printing searching status.
		else:                                           # Else then 
			print(" ", [r], "-->", [a[m]])              # Printing searching status.
			return m, r                                 # - return result.
	return -1, r

def visualization():
	from random import randint                           # Importing randint item in random module.
	n = 10                                               # Choice random length of list.
	a = [i for i in range(0, n)]                         # Filling list from 0 to n numbers.
	x = randint(0, n - 1)                                # Create random numbers for searching.
	print("Initial list:", a)                            # Printing initial list.
	print("The number of which must be found:", x)       # Printing searching number.
	print("Visualization of algorithm work.")            # Printing decription.
	r, i = interpolationsearch(a, x)                     # Searching number.
	if r != -1:                                          # If result there is then 
		print("Result of searching: ", r)                # - printing result,
	else:										         # Else then 
		print("This number does not exist in the list.") # - printing that result no exist.
	print("Total numbers of passages:", i)               # Printing numbers of passages.

import timeit
elapsed_time = timeit.timeit(visualization, number = 1) # Start program and counting elapsed time.
print("Elapsed time: ", round(elapsed_time, 3), "sec.") # Printing elapsed time.