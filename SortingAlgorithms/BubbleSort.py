def bubbleSort(collection):
	length = len(collection)
	for i in range(0, length - 1):
		isSorted = True
		for j in range(0, length - 1):
			if collection[j] > collection[j + 1]:
				temp = collection[j]
				collection[j] = collection[j + 1]
				collection[j + 1] = temp
				isSorted = False
		print(" ", [i + 1], "-->", collection)
		if isSorted:
			break

	return collection, i + 1

def visualization():
	from random import randint
	length = 10
	collection = [randint(0, length) for item in range(length)]

	print("Initial list:", collection)
	print("Visualization of algorithm work.")

	collection, counter = bubbleSort(collection)

	print("Final list:", collection)
	print("Total numbers of passages:", counter)

def main():
	import timeit
	elapsedTime = timeit.timeit(visualization, number = 1)
	print("Elapsed time: ", round(elapsedTime, 3), "sec.")

if __name__ == '__main__':
	main()