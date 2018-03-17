# --------------------
# Merge sort algortihm.
# --------------------

def mergesort(a, n):
	global s
	if len(a) > 1:                           # Checking the lenght of the list.
		m = len(a) // 2                      # Searching middle position of the list.
		l, r = a[:m], a[m:]                  # Searching start and finish position of the list.
		mergesort(l, n), mergesort(r, n)     # Recursion function for separation list at 1 item.
		i, j, k = 0, 0, 0                    # Indexes variables.
		while (i < len(l)) and (j < len(r)): # Passing through in l and r lists.
			if l[i] < r[j]:                  # If l[i] less r[j] then 
				a[k], i = l[i], i + 1        # - assign a[k] to l[i] and increment i,
			else:                            # Else then 
				a[k], j = r[j], j + 1        # - assign a[k] to r[j] and increment j.
			k += 1                           # Increment k for up position in list.
		while i < len(l):                    # Passing through in l list.
			a[k], i, k = l[i], i + 1, k + 1  # Assign a[k] to l[i], increments i, k.
		while j  < len(r):                   # Passing through in r list.
			a[k], j, k = r[j], j + 1, k + 1  # Assign a[k] to r[j], increments j, k.
		print(" ", [s], "-->", l, "<->", r)  # Printing sorting status.
		s += 1
	if len(a) == n:
		return a

def visualization():
	from random import randint                  # Importing randint item in random module.
	n = 10                                      # Amount items in list.
	a = [randint(0, n) for i in range(n)]       # Filling list of randoms numbers.
	print("Initial list:", a)                   # Printing initial list.
	print("Visualization of algorithm work.")   # Printing decription.
	a  = mergesort(a, n)                        # Sorting list.
	print("Final list:", a)                     # Printing final list.
	print("Total numbers of passages:", s - 1)  # Printing numbers of passages.

import timeit
s = 1
elapsed_time = timeit.timeit(visualization, number = 1) # Start program and counting elapsed time.
print("Elapsed time: ", round(elapsed_time, 3), "sec.") # Printing elapsed time.