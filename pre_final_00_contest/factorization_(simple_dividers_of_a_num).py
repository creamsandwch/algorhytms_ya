import sys


def factorize_number(number: int) -> str:
    divider = 2
    buffer = []

    while divider * divider <= number:
        if number % divider:
            divider += 1
        else:
            buffer.append(str(divider))
            number //= divider
    if number > 1:
        buffer.append(str(number))
    return ' '.join(buffer)


def prime_dividers(number):
    dividers = []
    while number % 2 == 0:
        dividers.append(2)
        number //= 2
    for i in range(3, int(number**0.5) + 1, 2):
        while number % i == 0:
            dividers.append(i)
            number //= i
    if number > 2:
        dividers.append(number)
    return ' '.join([str(x) for x in dividers])


def main():
    number = int(sys.stdin.readline().strip())
    sys.stdout.write(str(prime_dividers(number)))


if __name__ == '__main__':
    main()
