def bracket_generator(num: int, prefix='', cnt_in=0, cnt_out=0):
    print(f'start: num={num}, cnt_in, cnt_out = {cnt_in}, {cnt_out}')
    if cnt_in == num and cnt_out == num:
        print(prefix)
    else:
        if cnt_in < num:
            bracket_generator(num, prefix + '(', cnt_in + 1, cnt_out)
        if cnt_out < cnt_in:
            bracket_generator(num, prefix + ')', cnt_in, cnt_out + 1)


def main():
    n = int(input().strip())
    bracket_generator(num=n)


if __name__ == '__main__':
    main()
