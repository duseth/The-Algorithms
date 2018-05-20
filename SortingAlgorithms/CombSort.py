def combSort(initialList):
	global passingCounter
	lenghtList = len(initialList)
	gap = lenghtList * 10 // 13 if lenghtList > 1 else 0
	while gap:
		if 8 < gap < 11:
			gap = 11
		swapped = 0
		for index in range(lenghtList - gap):
			if initialList[index + gap] < initialList[index]:
				tempValue = initialList[index + gap]
				initialList[index + gap] = initialList[index]
				initialList[index] = tempValue
				swapped = 1
				print([passingCounter], "->", initialList)
				passingCounter += 1
		gap = (gap * 10 // 13) or swapped
	return initialList

def visualization():
	global passingCounter
	from random import randint
	lengthList = 10
	initialList = [randint(0, lengthList) for item in range(lengthList)]
	print("Initial list:", initialList)
	print("Visualization of algorithm work.")
	initialList = combSort(initialList)
	print("Final list:", initialList)
	print("Total numbers of passages:", passingCounter)

if __name__ == '__main__':
	import timeit
	passingCounter = 1
	elapsedTime = timeit.timeit(visualization, number = 1)
	print("Elapsed time: ", round(elapsedTime, 3), "sec.")