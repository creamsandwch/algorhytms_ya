def narcissistic(value: int):
    '''Checks whether given number is narcissistic
    (Armstrong number).'''
    str_value = str(value)
    length = len(str_value)

    narcissistic_sum = 0

    for num in str_value:
        narcissistic_sum += int(num) ** length

    return narcissistic_sum == value


def main():
    value = 153
    print(narcissistic(value))
    value = 1652
    print(narcissistic(value))
    value = 0
    print(narcissistic(value))


if __name__ == '__main__':
    main()
