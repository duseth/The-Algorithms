import timeit
from random import randint


def shell_sort(collection):
    length = len(collection)
    middle, counter = length // 2, 0

    while middle > 0:
        for i in range(0, length - middle):
            j = i
            while (j >= 0) and (collection[j] > collection[j + middle]):
                temp = collection[j]
                collection[j] = collection[j + middle]
                collection[j + middle] = temp

                j, counter = j - 1, counter + 1
                print("Step %i -->" % counter, collection)

        middle = middle // 2

    return collection, counter


def visualization():
    length = 10
    collection = [randint(0, length) for _ in range(length)]

    print("Initial list:", collection)
    print("Visualization of algorithm work.")

    collection, counter = shell_sort(collection)

    print("Final list:", collection)
    print("Total numbers of passages:", counter)


def main():
    elapsed_time = timeit.timeit(visualization, number=1)
    print("Elapsed time: ", round(elapsed_time, 7), "sec.")


if __name__ == '__main__':
    main()
