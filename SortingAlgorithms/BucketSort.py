import timeit
from random import randint


def bucket_sort(collection):
	length = len(collection)
	buckets_list = [0 for _ in range(length + 1)]

	print("\tBuckets list before sorting - {}".format(buckets_list))

	for j in range(length):
		buckets_list[collection[j]] += 1

	print("\tBuckets list after sorting - {}".format(buckets_list))

	counter = 0
	for i in range(length + 1):
		for j in range(buckets_list[i]):
			collection[counter] = i
			counter += 1

	return collection


def visualization():
	length = 10
	collection = [randint(0, length) for _ in range(length)]

	print("Initial list:", collection)
	print("Visualization of algorithm work.")

	collection = bucket_sort(collection)

	print("Final list:", collection)


def main():
	elapsed_time = timeit.timeit(visualization, number=1)
	print("Elapsed time: ", round(elapsed_time, 7), "sec.")


if __name__ == '__main__':
	main()
