# -----------------------
# Binary search algorithm.
# -----------------------

def binarysearch(a, x):
	i, u, r = 0, len(a), 1	                # Create start and finish position in list.
	while i != u:	                        # Passing through in list.
		c = (i + u) // 2                    # To divide list in 2 halfs.
		if x == a[c]:                       # Checking finding x if true then 
			print(" ", [r], "-->", [a[c]])  # - printing searching status.
			r += 1
			return c, r                     #  - return result.
		elif x < a[c]:                      # Else if x less a[c] then 
			u = c                           # - finish position variable equals c.
			print(" ", [r], "-->", a[:u])   # - printing searching status.
			r += 1
		else:                               # Else then 
			i = c + 1                       # - start position equals (c + 1).
			print(" ", [r], "-->", a[i:])   # - printing searching status.
			r += 1
	return -1, r

def visualization():
	from random import randint                           # Importing randint item in random module.
	n = 10                                               # Choice random length of list.
	a = [i for i in range(0, n)]                         # Filling list from 0 to n numbers.
	x = randint(0, n - 1)                                # Create random numbers for searching.
	print("Initial list:", a)                            # Printing initial list.
	print("The number of which must be found:", x)       # Printing searching number.
	print("Visualization of algorithm work.")            # Printing decription.
	r, i = binarysearch(a, x)                            # Searching number.
	if r != -1:                                          # If result there is then 
		print("Result of searching: ", r)                # - printing result,
	else:										         # Else then 
		print("This number does not exist in the list.") # - printing that result no exist.
	print("Total numbers of passages:", i)               # Printing numbers of passages.

import timeit
elapsed_time = timeit.timeit(visualization, number = 1) # Start program and counting elapsed time.
print("Elapsed time: ", round(elapsed_time, 3), "sec.") # Printing elapsed time.