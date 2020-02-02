import timeit
from random import randint


def gnome_sort(collection):
	length = len(collection)
	i, j, counter = 1, 2, 0

	while i < length:
		if collection[i - 1] < collection[i]:
			i, j = j, j + 1

			counter += 1
			print("Step %i -->" % counter, collection)
		else:
			collection[i], collection[i - 1] = collection[i - 1], collection[i]
			i -= 1
			if i == 0:
				i, j = j, j + 1

	return collection, counter


def visualization():
	length = 10
	collection = [randint(0, length) for _ in range(length)]

	print("Initial list:", collection)
	print("Visualization of algorithm work.")

	collection, counter = gnome_sort(collection)

	print("Final list:", collection)
	print("Total numbers of passages:", counter)


def main():
	elapsed_time = timeit.timeit(visualization, number=1)
	print("Elapsed time: ", round(elapsed_time, 7), "sec.")


if __name__ == '__main__':
	main()
