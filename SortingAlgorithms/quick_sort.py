import timeit
from random import randint


def partition(collection, left, right):
    pivot = collection[right]
    j = left
    for i in range(left, right):
        if collection[i] <= pivot:
            collection[i], collection[j] = collection[j], collection[i]
            j += 1
    collection[right], collection[j] = collection[j], collection[right]
    return j


def quickSort(collection, left, right, counter):
    if left < right:
        counter += 1
        print("Step %i -->" % counter, collection)

        mainstay = partition(collection, left, right)
        collection, counter = quickSort(collection, left, mainstay - 1, counter)
        collection, counter = quickSort(collection, mainstay + 1, right, counter)

    return collection, counter


def visualization():
    counter = 0
    length = 10
    collection = [randint(0, length) for _ in range(length)]

    print("Initial list:", collection)
    print("Visualization of algorithm work.")

    collection, counter = quickSort(collection, 0, length - 1, counter)

    print("Final list:", collection)
    print("Total numbers of passages:", counter)


def main():
    elapsedTime = timeit.timeit(visualization, number=1)
    print("Elapsed time: ", round(elapsedTime, 7), "sec.")


if __name__ == '__main__':
    main()
