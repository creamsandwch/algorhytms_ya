def get_input():
    count = int(input().strip())
    ppl = []
    for i in range(count):
        contestant = input().strip().split()
        ppl.append((
            contestant[0],
            (int(contestant[1]), int(contestant[2]))
        ))
    print(f'{ppl} - INIT')

    return ppl, count


def is_score_bigger(elem_1: tuple, elem_2: tuple, right=False):
    if elem_1[1][0] > elem_2[1][0]:
        return True
    elif elem_1[1][0] < elem_2[1][0]:
        return False
    else:
        if elem_1[1][1] < elem_2[1][1]:
            return True
        elif elem_1[1][1] == elem_2[1][1] and right:
            return True
        else:
            return False


def qsort_inplace(array, left, right):
    print(f'left, right: {left, right}')
    if right - left < 2:
        return
    else:
        pivot = (left + right) // 2

        saved_left, saved_right = left, right

        while left < right:
            left_is_bigger = is_score_bigger(array[left], array[pivot])
            right_is_smaller = is_score_bigger(array[pivot], array[right], True)

            if left_is_bigger and right_is_smaller:
                print(f'swap={array[left]} for {array[right]}, pivot is {array[pivot]}')
                array[left], array[right] = array[right], array[left]
                left += 1
                right -= 1
            else:
                if not left_is_bigger:
                    left += 1
                if not right_is_smaller:
                    right -= 1


        qsort_inplace(array, pivot, saved_right)
        qsort_inplace(array, saved_left, pivot)


def main():
    array, length = get_input()

    qsort_inplace(array, 0, length - 1)

    print(array, ' - AFTER')


    return array


if __name__ == '__main__':
    res = main()
    for elem in res:
        print(elem[0])
