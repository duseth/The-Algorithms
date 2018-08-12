def gnomeSort(collection):
	lenght = len(collection)
	i, j, counter = 1, 2, 0

	while i < lenght:
		if collection[i - 1] < collection[i]:
			i, j = j, j + 1

			counter += 1
			print(" ", [counter], "-->", collection)
		else:
			tempValue = collection[i]
			collection[i] = collection[i - 1]
			collection[i - 1] = tempValue
			i = i - 1
			if i == 0:
				i, j = j, j + 1

	return collection, counter

def visualization():
	from random import randint
	lenght = 10
	collection = [randint(0, lenght) for i in range(lenght)]

	print("Initial list:", collection)
	print("Visualization of algorithm work.")

	collection, counter = gnomeSort(collection)

	print("Final list:", collection)
	print("Total numbers of passages:", counter)

def main():
	import timeit
	elapsedTime = timeit.timeit(visualization, number = 1)
	print("Elapsed time: ", round(elapsedTime, 3), "sec.")

if __name__ == '__main__':
	main()