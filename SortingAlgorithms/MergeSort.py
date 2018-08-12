def mergesort(collection, lenght):
	global counter
	if len(collection) > 1:
		middlePosition = len(collection) // 2
		left = collection[:middlePosition]
		right = collection[middlePosition:]
		mergesort(left, lenght), mergesort(right, lenght)

		leftIndex, rightIndex, index = 0, 0, 0
		while (leftIndex < len(left)) and (rightIndex < len(right)):
			if left[leftIndex] < right[rightIndex]:
				collection[index] = left[leftIndex]
				leftIndex += 1
			else:
				collection[index] = right[rightIndex]
				rightIndex += 1
			index += 1

		while leftIndex < len(left):
			collection[index] = left[leftIndex]
			leftIndex += 1
			index += 1

		while rightIndex < len(right):
			collection[index] = right[rightIndex]
			rightIndex += 1
			index += 1

		print(" ", [counter], "-->", left, "<->", right)
		counter += 1

	if len(collection) == lenght:
		return collection

def visualization():
	from random import randint
	lenght = 10
	collection = [randint(0, lenght) for item in range(lenght)]

	print("Initial list:", collection)
	print("Visualization of algorithm work.")

	collection= mergesort(collection, lenght)

	print("Final list:", collection)
	print("Total numbers of passages:", counter - 1)

def main():
	import timeit
	counter = 1
	elapsedTime = timeit.timeit(visualization, number = 1)
	print("Elapsed time: ", round(elapsedTime, 3), "sec.")

if __name__ == '__main__':
	main()