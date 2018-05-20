def linearSearch(initialList, target):
	for index in range(0, len(initialList)):
		if initialList[index] == target:
			return index
	return -1

def visualization():
	from random import randint
	lengthList = 10
	initialList = [randint(0, lengthList) for index in range(0, lengthList)]
	target = randint(0, lengthList - 1)
	print("Initial list:", initialList)
	print("The number of which must be found:", target)
	searchingResult = linearSearch(initialList, target) 
	if searchingResult != -1:
		print("Result of searching: ", searchingResult)
	else:										 
		print("This number does not exist in the list.")

if __name__ == '__main__':
	import timeit
	elapsedTime = timeit.timeit(visualization, number = 1)
	print("Elapsed time: ", round(elapsedTime, 3), "sec.")