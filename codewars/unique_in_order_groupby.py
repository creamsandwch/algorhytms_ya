import sys
from itertools import groupby


def unique_in_order(sequence):
    grouped_tuple = groupby(sequence)
    out = []

    for key, iter_item in grouped_tuple:
        out.append(key)

    return out


def main():
    sequence = sys.stdin.readline().strip()
    sys.stdout.write(str(unique_in_order(sequence)))


if __name__ == '__main__':
    main()
