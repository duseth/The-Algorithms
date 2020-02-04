import timeit
from random import randint


def comb_sort(collection, counter):
	length = len(collection)
	gap = length * 10 // 13 if length > 1 else 0

	while gap:
		if 8 < gap < 11:
			gap = 11
		swapped = 0
		for index in range(length - gap):
			if collection[index + gap] < collection[index]:
				collection[index + gap], collection[index] = collection[index], collection[index + gap]
				swapped = 1

				counter += 1
				print("Step %i -->" % counter, collection)
		gap = (gap * 10 // 13) or swapped

	return collection, counter


def visualization():
	counter = 0
	length = 10
	collection = [randint(0, length) for _ in range(length)]

	print("Initial list:", collection)
	print("Visualization of algorithm work.")

	collection, counter = comb_sort(collection, counter)

	print("Final list:", collection)
	print("Total numbers of passages:", counter)


def main():
	elapsed_time = timeit.timeit(visualization, number=1)
	print("Elapsed time: ", round(elapsed_time, 7), "sec.")


if __name__ == '__main__':
	main()
