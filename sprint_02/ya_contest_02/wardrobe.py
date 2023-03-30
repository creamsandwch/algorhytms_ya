def get_input():
    arr_len = int(input().strip())
    arr = list(map(int, input().strip().split()))

    return arr, arr_len


def sort_by_order(arr, arr_len):
    less = []
    equal = []
    more = []

    for elem in arr:
        if elem < 1:
            less.append(elem)
        elif elem > 1:
            more.append(elem)
        else:
            equal.append(elem)

    return less + equal + more


def main():
    return sort_by_order(*get_input())


if __name__ == '__main__':
    print(' '.join(str(x) for x in main()))
