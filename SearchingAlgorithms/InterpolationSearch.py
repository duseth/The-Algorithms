# ------------------------------
# Interpolation search algorithm.
# ------------------------------

from random import randint                          # Importing randint item in random module.
n = randint(0, 25)                                  # Choice random length of list.
a = [i for i in range(0, n)]                        # Filling list from 0 to n numbers.
x, r = randint(0, n - 1), -1                        # Create random numbers for searching and result variable.
l, h = 0, len(a) - 1                                # Finding start and finish position.
while (a[l] < x) and (a[h] > x):                    # Passing through in list.
	m = l + ((x - a[l]) * (h - l)) // (a[h] - a[l]) # Finding middle position in list.
	if a[m] < x:                                    # If a[m] less x then 
		l = m + 1                                   # - assign l to (m + 1), 
	elif a[m] > x:                                  # Else if a[m] more x then 
		h = m - 1                                   # - assign h to (m - 1), 
	else:                                           # Else then 
		r = m                                       # - assign r to m,
		break                                       # - and break cycle.