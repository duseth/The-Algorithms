def linearSearch(collection, target):
	for i in range(0, len(collection)):
		if collection[i] == target:
			return i
	return -1

def visualization():
	from random import randint
	length = 10
	collection = [randint(0, length) for i in range(0, length)]
	target = randint(0, length - 1)

	print("Initial list:", collection)
	print("The number of which must be found:", target)

	result = linearSearch(collection, target) 
	if result != -1:
		print("Result of searching: ", result)
	else:										 
		print("This number does not exist in the list.")

def main():
	import timeit
	elapsedTime = timeit.timeit(visualization, number = 1)
	print("Elapsed time: ", round(elapsedTime, 3), "sec.")

if __name__ == '__main__':
	main()