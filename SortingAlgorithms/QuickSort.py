def partition(initialList, leftSide, rigthSide):
	pivot = initialList[rigthSide]
	supportIndex = leftSide
	for index in range(leftSide, rigthSide):
		if initialList[index] <= pivot:
			tempValue = initialList[index]
			initialList[index] = initialList[supportIndex]
			initialList[supportIndex] = tempValue
			supportIndex += 1
	tempValue = initialList[rigthSide]
	initialList[rigthSide] = initialList[supportIndex]
	initialList[supportIndex] = tempValue
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

if __name__ == '__main__':
	import timeit
	elapsedTime = timeit.timeit(visualization, number = 1)
	print("Elapsed time: ", round(elapsedTime, 3), "sec.")