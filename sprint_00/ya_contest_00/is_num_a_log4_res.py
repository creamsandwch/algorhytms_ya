import sys


def check_if_num_is_degree_of_four(num: int) -> bool:
    res = 4
    if num == 1:
        return True
    if num < 4:
        return False
    while res <= num:
        if res == num:
            return True
        res *= 4
    return False


def is_power_of_four(n: int) -> bool:
    if n <= 0:
        return False
    while n > 1:
        if n % 4 != 0:
            return False
        print('iter:', end=' ')
        print(f'before: n={n}')
        n //= 4
        print(f'after: n={n}')
        print()
    return n == 1


def main():
    num = int(sys.stdin.readline().strip())
    sys.stdout.write(str(check_if_num_is_degree_of_four(num)) + '\n')
    sys.stdout.write(str(is_power_of_four(num)))


if __name__ == '__main__':
    main()
