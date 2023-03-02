import sys


def unique_in_order(sequence):
    sequence = list(sequence)
    if len(sequence) == 0 or len(sequence) == 1:
        return sequence

    out = list()
    out.append(sequence[0])

    for i in range(1, len(sequence)):
        if sequence[i] != sequence[i - 1]:
            out.append(sequence[i])

    return out


def main():
    sequence = sys.stdin.readline().strip()
    sys.stdout.write(str(unique_in_order(sequence)))


if __name__ == '__main__':
    main()
