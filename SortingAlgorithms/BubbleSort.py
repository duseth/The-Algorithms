def bubbleSort(initialList):
	lengthList = len(initialList)
	for outsideIndex in range(0, lengthList - 1):
		isSorted = True
		for insideIndex in range(0, lengthList - 1):
			if initialList[insideIndex] > initialList[insideIndex + 1]:
				tempValue = initialList[insideIndex]
				initialList[insideIndex] = initialList[insideIndex + 1]
				initialList[insideIndex + 1] = tempValue
				isSorted = False
		print(" ", [outsideIndex + 1], "-->", initialList)
		if isSorted:
			break
	return initialList, outsideIndex + 1

def visualization():
	from random import randint
	lengthList = 10
	initialList = [randint(0, lengthList) for item in range(lengthList)]
	print("Initial list:", initialList)
	print("Visualization of algorithm work.")
	initialList, passingCounter = bubbleSort(initialList)
	print("Final list:", initialList)
	print("Total numbers of passages:", passingCounter)

if __name__ == '__main__':
	import timeit
	elapsedTime = timeit.timeit(visualization, number = 1)
	print("Elapsed time: ", round(elapsedTime, 3), "sec.")