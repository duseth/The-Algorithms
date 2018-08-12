def cocktailSort(collection):
	lenght = len(collection)
	left, right = 0, lenght - 1

	while left <= right:
		for i in range(left, right, +1):
			if collection[i] > collection[i + 1]:
				temp = collection[i]
				collection[i] = collection[i + 1]
				collection[i + 1] = temp

		right -= 1
		for i in range(right, left, -1):
			if collection[i - 1] > collection[i]:
				temp = collection[i]
				collection[i] = collection[i - 1]
				collection[i - 1] = temp
		left += 1
		print(" ", [left], "-->", collection)

	return collection, left

def visualization():
	from random import randint
	lenght = 10
	collection = [randint(0, lenght) for i in range(lenght)]

	print("Initial list:", collection)
	print("Visualization of algorithm work.")

	collection, passingCounter = cocktailSort(collection)

	print("Final list:", collection)
	print("Total numbers of passages:", passingCounter)

def main():
	import timeit
	elapsedTime = timeit.timeit(visualization, number = 1)
	print("Elapsed time: ", round(elapsedTime, 3), "sec.")

if __name__ == '__main__':
	main()