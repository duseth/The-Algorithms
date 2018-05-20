def gnomeSort(initialList):
	lengthList = len(initialList)
	index, supportIndex, passingCounter = 1, 2, 0
	while index < lengthList:
		if initialList[index - 1] < initialList[index]:
			index, supportIndex = supportIndex, supportIndex + 1
			passingCounter += 1
			print(" ", [passingCounter], "-->", initialList)
		else:
			tempValue = initialList[index]
			initialList[index] = initialList[index - 1]
			initialList[index - 1] = tempValue
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
	initialList, passingCounter = gnomeSort(initialList)
	print("Final list:", initialList)
	print("Total numbers of passages:", passingCounter)

if __name__ == '__main__':
	import timeit
	elapsedTime = timeit.timeit(visualization, number = 1)
	print("Elapsed time: ", round(elapsedTime, 3), "sec.")