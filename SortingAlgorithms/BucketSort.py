def bucketSort(initialList):
	lengthList = len(initialList)
	bucketsList = [0 for insideIndex in range(lengthList + 1)]
	print("  Buckets list before sorting - {}".format(bucketsList))
	for insideIndex in range(lengthList):
		bucketsList[initialList[insideIndex]] += 1
	print("  Buckets list after sorting - {}".format(bucketsList))
	counterNumbers = 0
	for outsideIndex in range(lengthList + 1):
		for insideIndex in range(bucketsList[outsideIndex]):
			initialList[counterNumbers] = outsideIndex
			counterNumbers += 1
	return initialList

def visualization():
	from random import randint
	lengthList = 10
	initialList = [randint(0, lengthList) for item in range(lengthList)]
	print("Initial list:", initialList)
	print("Visualization of algorithm work.")
	initialList = bucketSort(initialList)
	print("Final list:", initialList)

if __name__ == '__main__':
	import timeit
	elapsedTime = timeit.timeit(visualization, number = 1)
	print("Elapsed time: ", round(elapsedTime, 3), "sec.")