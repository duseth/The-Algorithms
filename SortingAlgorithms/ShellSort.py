def shellSort(initialList):
	lengthList = len(initialList)
	middlePosition, passingCounter = lengthList // 2, 0
	while middlePosition > 0:
		for index in range(0, lengthList - middlePosition):
			supportIndex = index
			while (supportIndex >= 0) and (initialList[supportIndex] > initialList[supportIndex + middlePosition]):
				tempValue = initialList[supportIndex]
				initialList[supportIndex] = initialList[supportIndex + middlePosition]
				initialList[supportIndex + middlePosition] = tempValue
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
	initialList, passingCounter = shellSort(initialList)
	print("Final list:", initialList)
	print("Total numbers of passages:", passingCounter)

if __name__ == '__main__':
	import timeit
	elapsedTime = timeit.timeit(visualization, number = 1)
	print("Elapsed time: ", round(elapsedTime, 3), "sec.")