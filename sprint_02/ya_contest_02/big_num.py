from functools import cmp_to_key


def get_input():
    num_count = int(input().strip())
    array = input().strip().split()
    return num_count, array


def compare_num_combinations(num_1, num_2):
    one_two = num_1 + num_2
    two_one = num_2 + num_1
    if one_two > two_one:
        return 1
    return -1


def main():
    num_count, array = get_input()

    array.sort(key=cmp_to_key(compare_num_combinations), reverse=True)
    print(''.join(array))


if __name__ == '__main__':
    main()
