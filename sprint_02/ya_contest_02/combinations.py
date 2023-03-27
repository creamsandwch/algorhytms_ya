numpad = {
        2: 'abc',
        3: 'def',
        4: 'ghi',
        5: 'jkl',
        6: 'mno',
        7: 'pqrs',
        8: 'tuv',
        9: 'wxyz'
    }


def get_combination(line: list, prefix='', index=0):
    if len(prefix) == len(line):
        print(prefix, end=' ')
    else:
        for i in range(len(numpad[line[index]])):
            get_combination(line, prefix + numpad[line[index]][i], index + 1)


def main():
    line = [int(x) for x in input().strip()]
    get_combination(line)


if __name__ == '__main__':
    main()
