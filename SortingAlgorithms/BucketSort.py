# ------------------
# Bucketsort algorithm.
# ------------------

def bucketsort(a, n):
	buckets = [0 for i in range(n + 1)]                    # Filling list of with zeros.
	print("  Buckets before sorting - {}".format(buckets)) # Printing buckets list before sorting.
	for i in range(n):                                     # Passing through in buckets list for sorting.
		buckets[a[i]] += 1                                 # Increment a[i] element in buckets for counting amount these numbers.
	print("  Buckets after sorting - {}".format(buckets))  # Printing buckets list after sorting.
	k = 0                                                  # Zeroing out.
	for j in range(n + 1):                                 # Passing through in main list for sorting.
		for i in range(buckets[j]):                        # Passing through in buckets list.
			a[k], k = j, k + 1                             # Assign a[k] to j and increment k for passing.
	return a                                               # Return sorted list.

def visualization():
	from random import randint                  # Importing randint item in random module.
	n = 10                                      # Amount items in list.
	a = [randint(0, n) for i in range(n)]       # Filling list of randoms numbers.
	print("Initial list:", a)                   # Printing initial list.
	print("Visualization of algorithm work.")   # Printing decription.
	a = bucketsort(a, n)                        # Sorting list.
	print("Final list:", a)                     # Printing final list.

import timeit
elapsed_time = timeit.timeit(visualization, number = 1) # Start program and counting elapsed time.
print("Elapsed time: ", round(elapsed_time, 3), "sec.") # Printing elapsed time.