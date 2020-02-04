import timeit
from random import randint


def stooge_sort(collection, left, right, counter):
    if left >= right:
        return

    if collection[right] < collection[left]:
        collection[left], collection[right] = collection[right], collection[left]

        counter += 1
        print("Step %i -->" % counter, collection)

    if (right - left + 1) > 2:
        list_part = (right - left + 1) // 3
        counter = stooge_sort(collection, left, right - list_part, counter)
        counter = stooge_sort(collection, left + list_part, right, counter)
        counter = stooge_sort(collection, left, right - list_part, counter)

    return counter


def visualization():
    counter = 0
    length_list = 10
    collection = [randint(0, length_list) for _ in range(length_list)]

    print("Initial list:", collection)
    print("Visualization of algorithm work.")

    counter = stooge_sort(collection, 0, length_list - 1, counter)

    print("Final list:", collection)
    print("Total numbers of passages:", counter)


def main():
    elapsed_time = timeit.timeit(visualization, number=1)
    print("Elapsed time: ", round(elapsed_time, 7), "sec.")


if __name__ == '__main__':
    main()
