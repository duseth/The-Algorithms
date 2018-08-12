def stoogeSort(collection, left, right):
	global counter

	if collection[right] < collection[left]:
		temp = collection[left]
		collection[left] = collection[right]
		collection[right] = temp

		print([counter], "-->", collection)
		counter += 1

	if (right - left + 1) > 2:
		listPart = (right - left + 1) // 3
		stoogeSort(collection, left, right - listPart)
		stoogeSort(collection, left + listPart, right)
		stoogeSort(collection, left, right - listPart)

	return collection

def visualization():
	from random import randint
	global counter
	lengthList = 10
	collection = [randint(0, lengthList) for item in range(lengthList)]

	print("Initial list:", collection)
	print("Visualization of algorithm work.")

	collection = stoogeSort(collection, 0, lengthList - 1)

	print("Final list:", collection)
	print("Total numbers of passages:", counter)

def main():
	import timeit
	counter = 1
	elapsedTime = timeit.timeit(visualization, number = 1)
	print("Elapsed time: ", round(elapsedTime, 3), "sec.")

if __name__ == '__main__':
	main()