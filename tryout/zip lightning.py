def get_input():
    length = int(input().strip())
    array_1 = input().strip().split()
    array_2 = input().strip().split()
    return length, array_1, array_2


length, array_1, array_2 = get_input()


def result(length, array_1, array_2):
    for i in range(0, length):
        print(array_1[i] + ' ' + array_2[i], end=' ')


result(length, array_1, array_2)
