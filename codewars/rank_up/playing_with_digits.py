def dig_pow(n: int, p: int):
    str_n = str(n)
    sum_to_comp = 0

    for num in str_n:
        sum_to_comp += int(num) ** (p)
        p += 1

    if sum_to_comp % n == 0:
        return sum_to_comp // n
    return -1


def main():
    print(dig_pow(89, 1))
    print(dig_pow(92, 1))
    print(dig_pow(46288, 3))
    print(dig_pow(41, 5))
    print(dig_pow(114, 3))
    print(dig_pow(8, 3))


if __name__ == '__main__':
    main()
