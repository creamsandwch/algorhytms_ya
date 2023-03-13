def get_input():
    row_count = int(input())
    col_count = int(input())
    matrix = []
    for i in range(row_count):
        line = input().strip().split()
        matrix.append(line)
    return row_count, col_count, matrix


def matrix_transpose(n, m, matrix: list):
    transposed_matrix = []
    for j in range(m):
        transposed_matrix.append([matrix[x][j] for x in range(n)])

    return transposed_matrix


def matrix_format(matrix):
    for row in matrix:
        for elem in row:
            print(elem, end=' ')
        print('\n', end='')


def main():
    matrix_format(matrix_transpose(*get_input()))


if __name__ == '__main__':
    main()
