def insertionSort(initialList):
	lengthList = len(initialList)
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
	initialList, index = insertionSort(initialList)
	print("Final list:", initialList) 
	print("Total numbers of passages:", index)

if __name__ == '__main__':
	import timeit
	elapsedTime = timeit.timeit(visualization, number = 1)
	print("Elapsed time: ", round(elapsedTime, 3), "sec.")