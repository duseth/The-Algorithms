# Ilyas Salimov, 2018
# Implemented on Python 3.5.2
# My understanding of this algorithm.

def selectionSort(initialList, lengthList):
	for outsideIndex in range(0, lengthList - 1):
		supportIndex = outsideIndex
		for insidexIndex in range(outsideIndex + 1, lengthList):
			if initialList[insidexIndex] < initialList[supportIndex]:
				supportIndex = insidexIndex
		initialList[outsideIndex], initialList[supportIndex] = initialList[supportIndex], initialList[outsideIndex]
		print(" ", [outsideIndex + 1], "-->", initialList)
	return initialList, outsideIndex + 1

def visualization():
	from random import randint
	lengthList = 10
	initialList = [randint(0, lengthList) for item in range(lengthList)]
	print("Initial list:", initialList)
	print("Visualization of algorithm work.")
	initialList, outsideIndex = selectionSort(initialList, lengthList)
	print("Final list:", initialList)
	print("Total numbers of passages:", outsideIndex)

import timeit
elapsedTime = timeit.timeit(visualization, number = 1)
print("Elapsed time: ", round(elapsedTime, 3), "sec.")