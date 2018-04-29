# Ilyas Salimov, 2018
# Implemented on Python 3.5.2
# My understanding of this algorithm.

def gnomeSort(initialList, lengthList):
	index, supportIndex, passingCounter = 1, 2, 0
	while index < lengthList:
		if initialList[index - 1] < initialList[index]:
			index, supportIndex, passingCounter = supportIndex, supportIndex + 1, passingCounter + 1
			print(" ", [passingCounter], "-->", initialList)
		else:
			initialList[index], initialList[index - 1] = initialList[index - 1], initialList[index]
			index = index - 1
			if index == 0:
				index, supportIndex = supportIndex, supportIndex + 1
	return initialList, passingCounter

def visualization():
	from random import randint
	lengthList = 10
	initialList = [randint(0, lengthList) for index in range(lengthList)]
	print("Initial list:", initialList)
	print("Visualization of algorithm work.")
	initialList, passingCounter = gnomeSort(initialList, lengthList)
	print("Final list:", initialList)
	print("Total numbers of passages:", passingCounter)

import timeit
elapsedTime = timeit.timeit(visualization, number = 1)
print("Elapsed time: ", round(elapsedTime, 3), "sec.")