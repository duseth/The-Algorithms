# --------------------
# Gnome sort algorithm.
# --------------------

from random import randint              # Importing randint item in random module.
n = 10                                  # Amount items in list.
a = [randint(0, n) for i in range(n)]   # Filling list of randoms numbers.
i, j = 1, 2                             # Assign i to 1 and j to 2 for working amid items the list.
while i < n:                           	# Passing through in list.     
	if a[i - 1] < a[i]:                 # If a[i - 1] less a[i] then
		i, j = j, j + 1                 # - assign i to j and increment j.
	else:                               # Else then
		a[i], a[i - 1] = a[i - 1], a[i] # - swap a[i] and a[i - 1],
		i -= 1                          # - decrement i.
		if i == 0:                      # If end of list then
			i, j = j, j + 1             # assign i to j and increment j.