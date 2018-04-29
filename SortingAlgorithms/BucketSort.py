# Ilyas Salimov, 2018
# Implemented on Python 3.5.2
# My understanding of this algorithm.

def bucketSort(initialList, lengthList):
	bucketsList = [0 for insideIndex in range(lengthList + 1)]
	print("  Buckets list before sorting - {}".format(bucketsList))
	for insideIndex in range(lengthList):
		bucketsList[initialList[insideIndex]] += 1
	print("  Buckets list after sorting - {}".format(bucketsList))
	counterNumbers = 0
	for outsideIndex in range(lengthList + 1):
		for insideIndex in range(bucketsList[outsideIndex]):
			initialList[counterNumbers], counterNumbers = outsideIndex, counterNumbers + 1
	return initialList

def visualization():
	from random import randint
	lengthList = 10
	initialList = [randint(0, lengthList) for insideIndex in range(lengthList)]
	print("Initial list:", initialList)
	print("Visualization of algorithm work.")
	initialList = bucketSort(initialList, lengthList)
	print("Final list:", initialList)

import timeit
elapsedTime = timeit.timeit(visualization, number = 1)
print("Elapsed time: ", round(elapsedTime, 3), "sec.")