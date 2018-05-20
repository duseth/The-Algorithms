def interpolationSearch(initialList, target):
	leftSide, rigthSide, passingCounter = 0, len(initialList) - 1, 1
	while (initialList[leftSide] <= target) and (initialList[rigthSide] >= target):
		middlePosition = leftSide + ((target - initialList[leftSide]) * (rigthSide - leftSide)) // (initialList[rigthSide] - initialList[leftSide])
		if initialList[middlePosition] < target:
			leftSide = middlePosition + 1
			print(" ", [passingCounter], "-->", initialList[leftSide:])
			passingCounter += 1
		elif initialList[middlePosition] > target:
			rigthSide = middlePosition - 1
			print(" ", [passingCounter], "-->", initialList[:rigthSide])
			passingCounter += 1
		else:
			print(" ", [passingCounter], "-->", [initialList[middlePosition]])
			passingCounter += 1
			return middlePosition, passingCounter
	return -1, passingCounter

def visualization():
	from random import randint
	lengthList = 10
	initialList = [item for item in range(0, lengthList)]
	target = randint(0, lengthList - 1)
	print("Initial list:", initialList)
	print("The number of which must be found:", target)
	print("Visualization of algorithm work.")
	searchingResult, passingCounter = interpolationSearch(initialList, target)
	if searchingResult != -1:
		print("Result of searching: ", searchingResult)
	else:
		print("This number does not exist in the list.")
	print("Total numbers of passages:", passingCounter)

if __name__ == '__main__':
	import timeit
	elapsedTime = timeit.timeit(visualization, number = 1)
	print("Elapsed time: ", round(elapsedTime, 3), "sec.")