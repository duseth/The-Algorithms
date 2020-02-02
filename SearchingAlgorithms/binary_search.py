import timeit
from random import randint


def binary_search(collection, target):
	left, right, counter = 0, len(collection), 0
	while left != right:	
		c = (left + right) // 2
		if target == collection[c]:
			counter += 1
			print("Step %i -->" % counter, [collection[c]])
			return c, counter
		elif target < collection[c]:
			counter += 1
			right = c
			print("Step %i -->" % counter, collection[:right])
		else:
			counter += 1
			left = c + 1
			print("Step %i -->" % counter, collection[left:])

	return -1, counter


def visualization():
	length = 10 
	collection = [item for item in range(0, length)]
	target = randint(0, length - 1)

	print("Initial list:", collection)
	print("The number of which must be found:", target)
	print("Visualization of algorithm work.")

	result, counter = binary_search(collection, target)
	if result != -1:
		print("Result of searching:", result)
	else:
		print("This number does not exist in the list.")

	print("Total numbers of passages:", counter)


def main():
	elapsed_time = timeit.timeit(visualization, number=1)
	print("Elapsed time: ", round(elapsed_time, 7), "sec.")


if __name__ == '__main__':
	main()
