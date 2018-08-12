def insertionSort(collection):
	lenght = len(collection)
	for i in range(0, lenght):
		value = collection[i]
		j = i
		while (j > 0) and (collection[j - 1] > value):
			collection[j] = collection[j - 1]
			j -= 1
		collection[j] = value

		print(" ", [i + 1], "-->", collection)

	return collection, i + 1

def visualization():
	from random import randint
	lenght = 10
	collection = [randint(0, lenght) for i in range(lenght)]

	print("Initial list:", collection)
	print("Visualization of algorithm work.")

	collection, i = insertionSort(collection)

	print("Final list:", collection) 
	print("Total numbers of passages:", i)

def main():
	import timeit
	elapsedTime = timeit.timeit(visualization, number = 1)
	print("Elapsed time: ", round(elapsedTime, 3), "sec.")

if __name__ == '__main__':
	main()