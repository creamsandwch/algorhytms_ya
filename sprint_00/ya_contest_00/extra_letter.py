import sys


def find_extra_letter(s1: str, s2: str):
    s2_list = list(s2)
    for elem in s1:
        s2_list.remove(elem)
    return s2_list[0]


def main():
    s = sys.stdin.readline().strip()
    t = sys.stdin.readline().strip()
    sys.stdout.write(find_extra_letter(s, t))


if __name__ == '__main__':
    main()
