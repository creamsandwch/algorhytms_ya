import sys


def get_input():
    a = sys.stdin.readline().strip()[::-1]
    b = sys.stdin.readline().strip()[::-1]
    if len(a) >= len(b):
        b += '0' * (len(a) - len(b))
        return a, b
    a += '0' * (len(b) - len(a))
    return b, a


def binary_sum(first_num: str, second_num: str) -> str:
    if first_num == second_num == '0':
        return str(0)
    first_num_int_list = [int(x) for x in first_num]
    second_num_int_list = [int(x) for x in second_num]
    result = ''
    head = 0

    for i in range(len(first_num_int_list)):
        step_result = (first_num_int_list[i] + second_num_int_list[i] + head)
        head = 0
        if step_result >= 2:
            head = 1
        result += str(step_result % 2)

    if i == len(first_num_int_list) - 1:
        result += str(head) * head

    return result[::-1]


def main():
    sys.stdout.write(binary_sum(*get_input()))


if __name__ == '__main__':
    main()
