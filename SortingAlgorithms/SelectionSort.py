def selectionSort(collection):
	lengthList = len(collection)
	for i in range(0, lengthList - 1):
		j = i
		for insidexIndex in range(i + 1, lengthList):
			if collection[insidexIndex] < collection[j]:
				j = insidexIndex
		temp = collection[j]
		collection[j] = collection[i]
		collection[i] = temp

		print(" ", [i + 1], "-->", collection)

	return collection, i + 1

def visualization():
	from random import randint
	lengthList = 10
	collection = [randint(0, lengthList) for item in range(lengthList)]

	print("Initial list:", collection)
	print("Visualization of algorithm work.")

	collection, i = selectionSort(collection)

	print("Final list:", collection)
	print("Total numbers of passages:", i)

def main():
	import timeit
	elapsedTime = timeit.timeit(visualization, number = 1)
	print("Elapsed time: ", round(elapsedTime, 3), "sec.")

if __name__ == '__main__':
	main()