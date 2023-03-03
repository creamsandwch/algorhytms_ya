import sys


def maskify(cc):
    count = 0
    if len(cc) <= 4:
        return cc
    for i in range(len(cc) - 4):
        print(f'step {count}: i={i}')
        cc[i] = '#'
        count += 1
    return ''.join(str(x) for x in cc)


def main():
    cc = list(sys.stdin.readline().strip())
    sys.stdout.write(str(maskify(cc)))


if __name__ == '__main__':
    main()
