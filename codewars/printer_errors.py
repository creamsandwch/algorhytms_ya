import sys


def printer_error(cc: str) -> str:
    cc_list = list(cc)
    for char in cc:
        if char in 'abcdefghijklm':
            cc_list.remove(char)
    return f'{len(cc_list)}/{len(cc)}'


def main():
    cc = sys.stdin.readline().strip()
    sys.stdout.write(str(printer_error(cc=cc)))


if __name__ == '__main__':
    main()
