def partition(collection, left, right):
	pivot = collection[right]
	j = left
	for i in range(left, right):
		if collection[i] <= pivot:
			temp = collection[i]
			collection[i] = collection[j]
			collection[j] = temp
			j += 1
	temp = collection[right]
	collection[right] = collection[j]
	collection[j] = temp

	return j

def quickSort(collection, left, right):
	global counter

	if left < right:
		counter += 1
		print(" ", [counter], "-->", collection)

		mainstay = partition(collection, left, right)
		quickSort(collection, left, mainstay - 1)
		quickSort(collection, mainstay + 1, right)

	return collection

def visualization():
	global counter
	from random import randint
	lengthList = 10
	collection = [randint(0, lengthList) for item in range(lengthList)]

	print("Initial list:", collection)
	print("Visualization of algorithm work.")

	counter = 0
	collection = quickSort(collection, 0, lengthList - 1)

	print("Final list:", collection)
	print("Total numbers of passages:", counter)

def main():
	import timeit
	elapsedTime = timeit.timeit(visualization, number = 1)
	print("Elapsed time: ", round(elapsedTime, 3), "sec.")

if __name__ == '__main__':
	main()