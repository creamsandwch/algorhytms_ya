import sys


def decimal_to_binary():
    decimal = int(sys.stdin.readline().strip())
    binary = ''
    if decimal == 0:
        return decimal
    while decimal > 0:
        binary += str(decimal % 2)
        decimal = decimal // 2
    return binary[::-1]


def main():
    sys.stdout.write(str(decimal_to_binary()))


if __name__ == '__main__':
    main()
