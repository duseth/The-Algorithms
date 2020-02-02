import timeit
from random import randint


def bubble_sort(collection):
	counter = 0
	length = len(collection)
	for i in range(0, length - 1):
		is_sorted = True
		for j in range(0, length - 1):
			if collection[j] > collection[j + 1]:
				collection[j], collection[j + 1] = collection[j + 1], collection[j]
				is_sorted = False
		counter += 1
		print("Step %i -->" % counter, collection)
		if is_sorted:
			break

	return collection, counter


def visualization():
	length = 10
	collection = [randint(0, length) for _ in range(length)]

	print("Initial list:", collection)
	print("Visualization of algorithm work.")

	collection, counter = bubble_sort(collection)

	print("Final list:", collection)
	print("Total numbers of passages:", counter)


def main():
	elapsed_time = timeit.timeit(visualization, number=1)
	print("Elapsed time: ", round(elapsed_time, 7), "sec.")


if __name__ == '__main__':
	main()
