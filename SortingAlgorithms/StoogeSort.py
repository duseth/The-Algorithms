# Ilyas Salimov, 2018
# Implemented on Python 3.5.2
# My understanding of this algorithm.

def stoogeSort(initialList, leftSide, rightSide):
	global passingCounter
	if initialList[rightSide] < initialList[leftSide]:
		initialList[rightSide], initialList[leftSide] = initialList[leftSide], initialList[rightSide]
		print([passingCounter], "-->", initialList)
		passingCounter += 1
	if (rightSide - leftSide + 1) > 2:
		listPart = (rightSide - leftSide + 1) // 3
		stoogeSort(initialList, leftSide, rightSide - listPart)
		stoogeSort(initialList, leftSide + listPart, rightSide)
		stoogeSort(initialList, leftSide, rightSide - listPart)
	return initialList

def visualization():
	from random import randint
	global passingCounter
	lengthList = 10
	initialList = [randint(0, lengthList) for item in range(lengthList)]
	print("Initial list:", initialList)
	print("Visualization of algorithm work.")
	initialList = stoogeSort(initialList, 0, lengthList - 1)
	print("Final list:", initialList)
	print("Total numbers of passages:", passingCounter)

import timeit
passingCounter = 1
elapsedTime = timeit.timeit(visualization, number = 1)
print("Elapsed time: ", round(elapsedTime, 3), "sec.")