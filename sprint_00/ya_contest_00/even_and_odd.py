import sys


def get_input():
    line = sys.stdin.readline().rstrip()
    a, b, c = line.split()
    a = int(a)
    b = int(b)
    c = int(c)
    return a, b, c


def check_all_for_odd_or_even(a, b, c):
    if (
        bool(a % 2) == bool(b % 2) == bool(c % 2)
    ):
        return 'WIN'
    return 'FAIL'


def main():
    sys.stdout.write(check_all_for_odd_or_even(*get_input()))


if __name__ == '__main__':
    main()
