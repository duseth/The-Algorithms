def bucketSort(collection):
	length = len(collection)
	bucketsList = [0 for j in range(length + 1)]

	print("  Buckets list before sorting - {}".format(bucketsList))

	for j in range(length):
		bucketsList[collection[j]] += 1

	print("  Buckets list after sorting - {}".format(bucketsList))

	counter = 0
	for i in range(length + 1):
		for j in range(bucketsList[i]):
			collection[counter] = i
			counter += 1

	return collection

def visualization():
	from random import randint
	length = 10
	collection = [randint(0, length) for item in range(length)]

	print("Initial list:", collection)
	print("Visualization of algorithm work.")

	collection = bucketSort(collection)

	print("Final list:", collection)

def main():
	import timeit
	elapsedTime = timeit.timeit(visualization, number = 1)
	print("Elapsed time: ", round(elapsedTime, 3), "sec.")

if __name__ == '__main__':
	main()