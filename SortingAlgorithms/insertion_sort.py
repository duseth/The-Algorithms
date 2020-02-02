import timeit
from random import randint


def insertion_sort(collection):
	counter = 0
	length = len(collection)
	for i in range(0, length):
		value = collection[i]
		j = i
		while (j > 0) and (collection[j - 1] > value):
			collection[j] = collection[j - 1]
			j -= 1
		collection[j] = value

		counter += 1
		print("Step %i -->" % counter, collection)

	return collection, counter


def visualization():
	length = 10
	collection = [randint(0, length) for _ in range(length)]

	print("Initial list:", collection)
	print("Visualization of algorithm work.")

	collection, counter = insertion_sort(collection)

	print("Final list:", collection) 
	print("Total numbers of passages:", counter)


def main():
	elapsed_time = timeit.timeit(visualization, number=1)
	print("Elapsed time: ", round(elapsed_time, 7), "sec.")


if __name__ == '__main__':
	main()
