def combSort(collection):
	global counter
	lenght = len(collection)
	gap = lenght * 10 // 13 if lenght > 1 else 0

	while gap:
		if 8 < gap < 11:
			gap = 11
		swapped = 0
		for index in range(lenght - gap):
			if collection[index + gap] < collection[index]:
				temp = collection[index + gap]
				collection[index + gap] = collection[index]
				collection[index] = temp
				swapped = 1

				print([counter], "->", collection)
				counter += 1
		gap = (gap * 10 // 13) or swapped

	return collection

def visualization():
	global counter
	from random import randint
	lenght = 10
	collection = [randint(0, lenght) for item in range(lenght)]

	print("Initial list:", collection)
	print("Visualization of algorithm work.")

	collection = combSort(collection)

	print("Final list:", collection)
	print("Total numbers of passages:", counter)

def main():
	import timeit
	counter = 1
	elapsedTime = timeit.timeit(visualization, number = 1)
	print("Elapsed time: ", round(elapsedTime, 3), "sec.")

if __name__ == '__main__':
	main()