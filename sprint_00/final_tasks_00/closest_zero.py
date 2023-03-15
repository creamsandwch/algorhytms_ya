# ID = 83283704

import sys


def get_input():
    street_length = int(sys.stdin.readline().strip())
    street = [int(x) for x in sys.stdin.readline().strip().split()]
    return street_length, street


def find_closest_zero(street_length: int, street: list) -> str:
    if len(street) == 1:
        return '0'

    closest_zeroes = [0 for x in range(street_length)]

    closest_zeroes[0] = 9**10

    if street[0] == 0:
        closest_zeroes[0] = 0

    for i in range(1, street_length):
        if street[i] == 0:
            closest_zeroes[i] = 0
        else:
            closest_zeroes[i] += closest_zeroes[i - 1] + 1

    if street[i - 1] == 0:
        closest_zeroes[i - 1] = 0

    for i in range(street_length - 2, -1, -1):
        if street[i] == 0:
            closest_zeroes[i] = 0
        else:
            closest_zeroes[i] = min(
                closest_zeroes[i], closest_zeroes[i + 1] + 1
            )

    return closest_zeroes


def main():
    print(*find_closest_zero(*get_input()))


if __name__ == '__main__':
    main()
