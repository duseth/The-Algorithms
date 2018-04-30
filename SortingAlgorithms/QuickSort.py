# Ilyas Salimov, 2018
# Implemented on Python 3.5.2
# My understanding of this algorithm.

def partition(initialList, leftSide, rigthSide):
	pivot = initialList[rigthSide]
	supportIndex = leftSide
	for index in range(leftSide, rigthSide):
		if initialList[index] <= pivot:
			initialList[supportIndex], initialList[index] = initialList[index], initialList[supportIndex]
			supportIndex += 1
	initialList[supportIndex], initialList[rigthSide] = initialList[rigthSide], initialList[supportIndex]
	return supportIndex

def quickSort(initialList, leftSide, rigthSide):
	global passingCounter
	if leftSide < rigthSide:
		passingCounter += 1
		print(" ", [passingCounter], "-->", initialList)
		mainstay = partition(initialList, leftSide, rigthSide)
		quickSort(initialList, leftSide, mainstay - 1)
		quickSort(initialList, mainstay + 1, rigthSide)
	return initialList

def visualization():
	global passingCounter
	from random import randint
	lengthList = 10
	initialList = [randint(0, lengthList) for item in range(lengthList)]
	print("Initial list:", initialList)
	print("Visualization of algorithm work.")
	passingCounter = 0
	initialList = quickSort(initialList, 0, lengthList - 1)
	print("Final list:", initialList)
	print("Total numbers of passages:", passingCounter)

import timeit
elapsedTime = timeit.timeit(visualization, number = 1)
print("Elapsed time: ", round(elapsedTime, 3), "sec.")