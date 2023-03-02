import sys


def if_isogram(cc: str) -> bool:
    if len(set(cc.lower())) == len(cc):
        return True
    return False


def main():
    cc = sys.stdin.readline().strip()
    sys.stdout.write(str(if_isogram(cc)))


if __name__ == '__main__':
    main()
