# --------------------
# Merge sort algortihm.
# --------------------

from random import randint                   # Importing randint item in random module.
n = 10                                       # Amount items in list.
a = [randint(0, n) for i in range(n)]        # Filling list of randoms numbers.
def mergeSort(a):                            # Create a merge sort function.
	if len(a) > 1:                           # Checking the lenght of the list.
		m = len(a) // 2                      # Searching middle position of the list.
		l, r = a[:m], a[m:]                  # Searching start and finish position of the list.
		mergeSort(l), mergeSort(r)           # Recursion function for separation list at 1 item.
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
mergeSort(a)                                 # Calling a function.