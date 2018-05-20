def mergesort(initialList, lengthList):
	global passingCounter
	if len(initialList) > 1:
		middlePosition = len(initialList) // 2
		leftSide = initialList[:middlePosition]
		rightSide = initialList[middlePosition:]
		mergesort(leftSide, lengthList), mergesort(rightSide, lengthList)

		leftIndex, rightIndex, index = 0, 0, 0
		while (leftIndex < len(leftSide)) and (rightIndex < len(rightSide)):
			if leftSide[leftIndex] < rightSide[rightIndex]:
				initialList[index] = leftSide[leftIndex]
				leftIndex += 1
			else:
				initialList[index] = rightSide[rightIndex]
				rightIndex += 1
			index += 1

		while leftIndex < len(leftSide):
			initialList[index] = leftSide[leftIndex]
			leftIndex += 1
			index += 1

		while rightIndex < len(rightSide):
			initialList[index] = rightSide[rightIndex]
			rightIndex += 1
			index += 1
		print(" ", [passingCounter], "-->", leftSide, "<->", rightSide)
		passingCounter += 1
	if len(initialList) == lengthList:
		return initialList

def visualization():
	from random import randint
	lengthList = 10
	initialList = [randint(0, lengthList) for item in range(lengthList)]
	print("Initial list:", initialList)
	print("Visualization of algorithm work.")
	initialList= mergesort(initialList, lengthList)
	print("Final list:", initialList)
	print("Total numbers of passages:", passingCounter - 1)

if __name__ == '__main__':
	import timeit
	passingCounter = 1
	elapsedTime = timeit.timeit(visualization, number = 1)
	print("Elapsed time: ", round(elapsedTime, 3), "sec.")