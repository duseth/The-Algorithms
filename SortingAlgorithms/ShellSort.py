def shellSort(collection):
	lengthList = len(collection)
	middle, counter = lengthList // 2, 0

	while middle > 0:
		for i in range(0, lengthList - middle):
			j = i
			while (j >= 0) and (collection[j] > collection[j + middle]):
				temp = collection[j]
				collection[j] = collection[j + middle]
				collection[j + middle] = temp

				j, counter = j - 1, counter + 1
				print(" ", [counter], "-->", collection)

		middle = middle // 2

	return collection, counter

def visualization():
	from random import randint
	lengthList = 10
	collection = [randint(0, lengthList) for i in range(lengthList)]

	print("Initial list:", collection)
	print("Visualization of algorithm work.")

	collection, counter = shellSort(collection)

	print("Final list:", collection)
	print("Total numbers of passages:", counter)

def main():
	import timeit
	elapsedTime = timeit.timeit(visualization, number = 1)
	print("Elapsed time: ", round(elapsedTime, 3), "sec.")

if __name__ == '__main__':
	main()