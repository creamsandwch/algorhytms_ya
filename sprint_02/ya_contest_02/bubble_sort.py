import sys


def bubble_sort(array: list):
    for i in range(len(array)):
        flag = False
        for j in range(1, len(array)):
            if array[j - 1] > array[j]:
                array[j], array[j - 1] = array[j - 1], array[j]
                flag = True
        if flag is False:
            break
        else:
            print(' '.join([str(x) for x in array]))
    return array


def main():
    sys.stdin.readline()
    line = sys.stdin.readline()
    init_array = [int(x) for x in line.strip().split()]
    array = [int(x) for x in line.strip().split()]

    if init_array == bubble_sort(array):
        print(' '.join(str(x) for x in init_array))


if __name__ == '__main__':
    main()
