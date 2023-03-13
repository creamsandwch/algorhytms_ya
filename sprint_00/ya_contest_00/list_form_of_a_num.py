import sys


def get_input():
    length = int(sys.stdin.readline().strip())
    number_list_form = sys.stdin.readline().strip().split()
    k = int(sys.stdin.readline().strip())
    return length, number_list_form, k


def sum_list_num_with_int_num(
        length: int, number_list_form: list, int_num: int
):
    result = ' '.join(str(int(''.join(number_list_form)) + int_num))
    return result


def main():
    sys.stdout.write(sum_list_num_with_int_num(*get_input()))


if __name__ == '__main__':
    main()
