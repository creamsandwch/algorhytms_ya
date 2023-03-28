import timeit

from itertools import permutations


def get_input():
    num_count = int(input().strip())
    array = input().strip().split()
    return num_count, array


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


def custom_permutations(array, index=0, res=[]):
    if index == len(array) - 1:
        res.append(int(''.join(array)))
    else:
        for i in range(index, len(array)):
            swap(array, index, i)
            permutations(array, index + 1)
            swap(array, index, i)

    return res


def main():
    num_count, array = get_input()

    start = timeit.default_timer()
    num_perms = list(permutations(array, r=num_count))
    num_perms = [int(''.join(x)) for x in num_perms]
    stop = timeit.default_timer()
    print(f'permutations time: {stop - start}')

    start = timeit.default_timer()
    max_num = max(num_perms)
    stop = timeit.default_timer()
    print(f'find max time: {stop - start}')

    return max_num


if __name__ == '__main__':
    print(main())
