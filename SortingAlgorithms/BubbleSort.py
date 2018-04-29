# Ilyas Salimov, 2018
# Implemented on Python 3.5.2
# My understanding of this algorithm.

def bubbleSort(initialList, lengthList):
	for outsideIndex in range(0, lengthList - 1):
		isSorted = 0
		for insideIndex in range(0, lengthList - 1):
			if initialList[insideIndex] > initialList[insideIndex + 1]:
				initialList[insideIndex], initialList[insideIndex + 1] = initialList[insideIndex + 1], initialList[insideIndex]
				isSorted = 1
		print(" ", [outsideIndex + 1], "-->", initialList)
		if isSorted == 0:
			break
	return initialList, outsideIndex + 1

def visualization():
	from random import randint
	lengthList = 10
	initialList = [randint(0, lengthList) for outsideIndex in range(lengthList)]
	print("Initial list:", initialList)
	print("Visualization of algorithm work.")
	initialList, passingCounter = bubbleSort(initialList, lengthList)
	print("Final list:", initialList)
	print("Total numbers of passages:", passingCounter)

import timeit
elapsedTime = timeit.timeit(visualization, number = 1)
print("Elapsed time: ", round(elapsedTime, 3), "sec.")