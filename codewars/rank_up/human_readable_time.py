def make_readable(seconds: int) -> str:
    ss = seconds % 60
    mm = seconds // 60 % 60
    hh = seconds // 3600
    return f'{hh:02}:{mm:02}:{ss:02}'


def main():
    print(make_readable(0))
    print(make_readable(5))
    print(make_readable(60))
    print(make_readable(86399))
    print(make_readable(359999))


if __name__ == '__main__':
    main()
