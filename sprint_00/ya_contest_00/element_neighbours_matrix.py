import sys


def get_input():
    n = int(input())
    m = int(input())
    matrix = list(list('*' for x in range(m + 2)) for y in range(n + 2))
    for i in range(n):
        line = sys.stdin.readline().strip().split()
        for j in range(m):
            matrix[i + 1][j + 1] = line[j]
    i = int(input()) + 1
    j = int(input()) + 1
    return i, j, matrix


def get_elem_neighbours(i, j, matrix):
    buffer_list = []
    indexes = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]

    for index in indexes:
        if matrix[index[0]][index[1]] != '*':
            buffer_list.append(int(matrix[index[0]][index[1]]))

    buffer_list.sort()
    print(*buffer_list, sep=' ')


def main():
    get_elem_neighbours(*get_input())


if __name__ == '__main__':
    main()
