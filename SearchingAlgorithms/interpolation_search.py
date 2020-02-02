import timeit
from random import randint


def interpolation_search(collection, target):
	left, right, counter = 0, len(collection) - 1, 0
	while (collection[left] <= target) and (collection[right] >= target):
		middle = left + ((target - collection[left]) * (right - left)) // (collection[right] - collection[left])
		if collection[middle] < target:
			counter += 1
			left = middle + 1
			print("Step %i -->" % counter, collection[left:])
		elif collection[middle] > target:
			counter += 1
			right = middle - 1
			print("Step %i -->" % counter, collection[:right])
		else:
			counter += 1
			print("Step %i -->" % counter, [collection[middle]])
			return middle, counter

	return -1, counter


def visualization():
	length = 10
	collection = [item for item in range(0, length)]
	target = randint(0, length - 1)

	print("Initial list:", collection)
	print("The number of which must be found:", target)
	print("Visualization of algorithm work.")

	result, counter = interpolation_search(collection, target)
	if result != -1:
		print("Result of searching: ", result)
	else:
		print("This number does not exist in the list.")

	print("Total numbers of passages:", counter)


def main():
	elapsed_time = timeit.timeit(visualization, number=1)
	print("Elapsed time: ", round(elapsed_time, 7), "sec.")


if __name__ == '__main__':
	main()
