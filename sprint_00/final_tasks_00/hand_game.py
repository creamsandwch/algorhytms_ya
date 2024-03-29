# ID = 83283733

import sys


def get_input():
    pressed_buttons_count = int(sys.stdin.readline().strip())
    field_numbers = []
    for i in range(4):
        field_numbers += [
            int(x) for x in sys.stdin.readline().strip().replace('.', '0')
        ]

    return pressed_buttons_count, field_numbers


def max_score(pressed_buttons_count, numbers):
    count = 0

    numbers_set = set(numbers)

    for i in range(1, 10):
        if numbers.count(i) <= pressed_buttons_count * 2 and i in numbers_set:
            count += 1

    return count


def main():
    sys.stdout.write(str(max_score(*get_input())))


if __name__ == '__main__':
    main()
