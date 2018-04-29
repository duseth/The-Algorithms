# Ilyas Salimov, 2018
# Implemented on Python 3.5.2
# My understanding of this algorithm.

def shellSort(initialList, lengthList):
	middlePosition, passingCounter = lengthList // 2, 0
	while middlePosition > 0:
		for index in range(0, lengthList - middlePosition):
			supportIndex = index
			while (supportIndex >= 0) and (initialList[supportIndex] > initialList[supportIndex + middlePosition]):
				initialList[supportIndex], initialList[supportIndex + middlePosition] = initialList[supportIndex + middlePosition], initialList[supportIndex]
				supportIndex, passingCounter = supportIndex - 1, passingCounter + 1
				print(" ", [passingCounter], "-->", initialList)
		middlePosition = middlePosition // 2
	return initialList, passingCounter

def visualization():
	from random import randint
	lengthList = 10
	initialList = [randint(0, lengthList) for index in range(lengthList)]
	print("Initial list:", initialList)
	print("Visualization of algorithm work.")
	initialList, passingCounter = shellSort(initialList, lengthList)
	print("Final list:", initialList)
	print("Total numbers of passages:", passingCounter)

import timeit
elapsedTime = timeit.timeit(visualization, number = 1)
print("Elapsed time: ", round(elapsedTime, 3), "sec.")