import sys


def get_input():
    line = sys.stdin.readline().rstrip()
    a, x, b, c = line.split()
    a = int(a)
    x = int(x)
    b = int(b)
    c = int(c)
    return a, x, b, c


def get_quadratic_func_result(a, x, b, c):
    return str(a * x**2 + b * x + c)


def main():
    sys.stdout.write(get_quadratic_func_result(*get_input()))


if __name__ == '__main__':
    main()
