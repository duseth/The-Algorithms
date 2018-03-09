# -----------------------
# Cocktail sort algortihm.
# -----------------------

from random import randint                  # Importing randint item in random module.
n = 10                                      # Amount items in list.
a = [randint(0, n) for i in range(n)]       # Filling list of randoms numbers.
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