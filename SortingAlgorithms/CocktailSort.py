# Ilyas Salimov, 2018
# Implemented on Python 3.5.2
# My understanding of this algorithm.

def cocktailSort(initialList, lengthList):
	leftSide, rightSide = 0, lengthList - 1
	while leftSide <= rightSide:
		for index in range(leftSide, rightSide, +1):
			if initialList[index] > initialList[index + 1]:
				initialList[index], initialList[index + 1] = initialList[index + 1], initialList[index]
		rightSide -= 1
		for index in range(rightSide, leftSide, -1):
			if initialList[index - 1] > initialList[index]:
				initialList[index], initialList[index - 1] = initialList[index - 1], initialList[index]
		leftSide += 1
		print(" ", [leftSide], "-->", initialList)
	return initialList, leftSide

def visualization():
	from random import randint
	lengthList = 10
	initialList = [randint(0, lengthList) for index in range(lengthList)]
	print("Initial list:", initialList)
	print("Visualization of algorithm work.")
	initialList, passingCounter = cocktailSort(initialList, lengthList)
	print("Final list:", initialList)
	print("Total numbers of passages:", passingCounter)

import timeit
elapsedTime = timeit.timeit(visualization, number = 1)
print("Elapsed time: ", round(elapsedTime, 3), "sec.")