import timeit
from random import randint


def selection_sort(collection):
    counter = 0
    length = len(collection)
    for i in range(0, length - 1):
        j = i
        for index in range(i + 1, length):
            if collection[index] < collection[j]:
                j = index
        collection[j], collection[i] = collection[i], collection[j]

        counter += 1
        print("Step %i -->" % counter, collection)

    return collection, counter


def visualization():
    length = 10
    collection = [randint(0, length) for _ in range(length)]

    print("Initial list:", collection)
    print("Visualization of algorithm work.")

    collection, counter = selection_sort(collection)

    print("Final list:", collection)
    print("Total numbers of passages:", counter)


def main():
    elapsed_time = timeit.timeit(visualization, number=1)
    print("Elapsed time: ", round(elapsed_time, 7), "sec.")


if __name__ == '__main__':
    main()
