# Ilyas Salimov, 2018
# Implemented on Python 3.5.2
# My understanding of this algorithm.

def insertionSort(initialList, lengthList):
	for index in range(0, lengthList):
		currentValue = initialList[index]
		currentIndex = index
		while (currentIndex > 0) and (initialList[currentIndex - 1] > currentValue):
			initialList[currentIndex] = initialList[currentIndex - 1]
			currentIndex -= 1
		initialList[currentIndex] = currentValue
		print(" ", [index + 1], "-->", initialList)
	return initialList, index + 1

def visualization():
	from random import randint
	lengthList = 10
	initialList = [randint(0, lengthList) for index in range(lengthList)]
	print("Initial list:", initialList)
	print("Visualization of algorithm work.")
	initialList, index = insertionSort(initialList, lengthList)
	print("Final list:", initialList) 
	print("Total numbers of passages:", index)

import timeit
elapsedTime = timeit.timeit(visualization, number = 1)
print("Elapsed time: ", round(elapsedTime, 3), "sec.")