import timeit
from random import randint


def stooge_sort(collection, left, right):
    global counter
    if left >= right:
        return

    if collection[right] < collection[left]:
        collection[left], collection[right] = collection[right], collection[left]

        counter += 1
        print("Step %i -->" % counter, collection)

    if (right - left + 1) > 2:
        list_part = (right - left + 1) // 3
        stooge_sort(collection, left, right - list_part)
        stooge_sort(collection, left + list_part, right)
        stooge_sort(collection, left, right - list_part)


def visualization():
    length_list = 10
    collection = [randint(0, length_list) for _ in range(length_list)]

    print("Initial list:", collection)
    print("Visualization of algorithm work.")

    stooge_sort(collection, 0, length_list - 1)

    print("Final list:", collection)
    print("Total numbers of passages:", counter)


def main():
    elapsed_time = timeit.timeit(visualization, number=1)
    print("Elapsed time: ", round(elapsed_time, 7), "sec.")


if __name__ == '__main__':
    counter = 0
    main()
