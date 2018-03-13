# -----------------------
# Binary search algorithm.
# -----------------------

from random import randint   # Importing randint item in random module.
n = randint(0, 25)           # Choice random length of list.
a = [i for i in range(0, n)] # Filling list from 0 to n numbers.
x, r = randint(0, n - 1), -1 # Create random numbers for searching and result variable.
i, u = 0, len(a)		     # Create start and finish position in list.
while i != u:	             # Passing through in list.
	c = (i + u) // 2         # To divide list in 2 halfs.
	if x == a[c]:            # Checking finding x if true then 
		r = c                # - result variable equals c and
		break                # - stop cycle.
	elif x < a[c]:           # Else if x less a[c] then 
		u = c                # - finish position variable equals c.
	else:                    # Else then 
		i = c + 1            # - start position equals (c + 1).