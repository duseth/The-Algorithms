def binarySearch(initialList, target):
	leftSide, rigthtSide, passingCounter = 0, len(initialList), 1
	while leftSide != rigthtSide:	
		c = (leftSide + rigthtSide) // 2
		if target == initialList[c]:
			print(" ", [passingCounter], "-->", [initialList[c]])
			passingCounter += 1
			return c, passingCounter
		elif target < initialList[c]:
			rigthtSide = c
			print(" ", [passingCounter], "-->", initialList[:rigthtSide])
			passingCounter += 1
		else: 
			leftSide = c + 1
			print(" ", [passingCounter], "-->", initialList[leftSide:])
			passingCounter += 1
	return -1, passingCounter

def visualization():
	from random import randint
	lengthList = 10 
	initialList = [leftSide for leftSide in range(0, lengthList)]
	target = randint(0, lengthList - 1)
	print("Initial list:", initialList)
	print("The number of which must be found:", target)
	print("Visualization of algorithm work.")
	searchingResult, passingCounter = binarySearch(initialList, target)
	if searchingResult != -1:
		print("Result of searching:", searchingResult)
	else:
		print("This number does not exist in the list.")
	print("Total numbers of passages:", passingCounter)

if __name__ == '__main__':
	import timeit
	elapsedTime = timeit.timeit(visualization, number = 1)
	print("Elapsed time: ", round(elapsedTime, 3), "sec.")