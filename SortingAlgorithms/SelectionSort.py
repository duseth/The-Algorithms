def selectionSort(initialList):
	lengthList = len(initialList)
	for outsideIndex in range(0, lengthList - 1):
		supportIndex = outsideIndex
		for insidexIndex in range(outsideIndex + 1, lengthList):
			if initialList[insidexIndex] < initialList[supportIndex]:
				supportIndex = insidexIndex
		tempValue = initialList[supportIndex]
		initialList[supportIndex] = initialList[outsideIndex]
		initialList[outsideIndex] = tempValue
		print(" ", [outsideIndex + 1], "-->", initialList)
	return initialList, outsideIndex + 1

def visualization():
	from random import randint
	lengthList = 10
	initialList = [randint(0, lengthList) for item in range(lengthList)]
	print("Initial list:", initialList)
	print("Visualization of algorithm work.")
	initialList, outsideIndex = selectionSort(initialList)
	print("Final list:", initialList)
	print("Total numbers of passages:", outsideIndex)

if __name__ == '__main__':
	import timeit
	elapsedTime = timeit.timeit(visualization, number = 1)
	print("Elapsed time: ", round(elapsedTime, 3), "sec.")