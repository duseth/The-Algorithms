def binarySearch(collection, target):
	left, right, counter = 0, len(collection), 1
	while left != right:	
		c = (left + right) // 2
		if target == collection[c]:
			print(" ", [counter], "-->", [collection[c]])
			counter += 1
			return c, counter
		elif target < collection[c]:
			right = c
			print(" ", [counter], "-->", collection[:right])
			counter += 1
		else: 
			left = c + 1
			print(" ", [counter], "-->", collection[left:])
			counter += 1

	return -1, counter

def visualization():
	from random import randint
	length = 10 
	collection = [left for left in range(0, length)]
	target = randint(0, length - 1)

	print("Initial list:", collection)
	print("The number of which must be found:", target)
	print("Visualization of algorithm work.")

	result, counter = binarySearch(collection, target)
	if result != -1:
		print("Result of searching:", result)
	else:
		print("This number does not exist in the list.")

	print("Total numbers of passages:", counter)

def main():
	import timeit
	elapsedTime = timeit.timeit(visualization, number = 1)
	print("Elapsed time: ", round(elapsedTime, 3), "sec.")

if __name__ == '__main__':
	main()