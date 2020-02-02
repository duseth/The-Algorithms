import timeit
from random import randint


def cocktail_sort(collection):
	counter = 0
	length = len(collection)
	left, right = 0, length - 1

	while left <= right:
		for i in range(left, right, +1):
			if collection[i] > collection[i + 1]:
				collection[i], collection[i + 1] = collection[i + 1], collection[i]

		right -= 1
		for i in range(right, left, -1):
			if collection[i - 1] > collection[i]:
				collection[i], collection[i - 1] = collection[i - 1], collection[i]
		left += 1
		counter += 1
		print("Step %i -->" % counter, collection)

	return collection, counter


def visualization():
	length = 10
	collection = [randint(0, length) for _ in range(length)]

	print("Initial list:", collection)
	print("Visualization of algorithm work.")

	collection, counter = cocktail_sort(collection)

	print("Final list:", collection)
	print("Total numbers of passages:", counter)


def main():
	elapsed_time = timeit.timeit(visualization, number=1)
	print("Elapsed time: ", round(elapsed_time, 7), "sec.")


if __name__ == '__main__':
	main()
