# --------------------
# Gnome sort algorithm.
# --------------------

def gnomesort(a, n):
	i, j, r = 1, 2, 0                       # Assign i to 1 and j to 2 for working amid items the list, r - counter.
	while i < n:                           	# Passing through in list.     
		if a[i - 1] < a[i]:                 # If a[i - 1] less a[i] then
			i, j, r = j, j + 1, r + 1       # - assign i to j and increment j, increment r.
			print(" ", [r], "-->", a)       # Printing sorting status.
		else:                               # Else then
			a[i], a[i - 1] = a[i - 1], a[i] # - swap a[i] and a[i - 1],
			i = i - 1                       # - decrement i.
			if i == 0:                      # If end of list then
				i, j = j, j + 1             # assign i to j and increment j.	
	return a, r                             # Return sorted list and number passages.

def visualization():
	from random import randint                  # Importing randint item in random module.
	n = 10                                      # Amount items in list.
	a = [randint(0, n) for i in range(n)]       # Filling list of randoms numbers.
	print("Initial list:", a)                   # Printing initial list.
	print("Visualization of algorithm work.")   # Printing decription.
	a, i = gnomesort(a, n)                      # Sorting list.
	print("Final list:", a)                     # Printing final list.
	print("Total numbers of passages:", i)      # Printing numbers of passages.

import timeit
elapsed_time = timeit.timeit(visualization, number = 1) # Start program and counting elapsed time.
print("Elapsed time: ", round(elapsed_time, 3), "sec.") # Printing elapsed time.