def get_input():
    length = int(input().strip())
    to_find = int(input().strip())
    nums = list(map(int, input().strip().split()))
    return nums, to_find, length


def start_search(nums, left, right):
    if right - left <= 1:
        return nums[right:] + nums[:left + 1]

    mid = (left + right) // 2

    if nums[mid] < nums[mid - 1]:
        return nums[mid:] + nums[:mid], mid
    else:
        start_search(nums, left, mid)
        start_search(nums, mid, right)
    return nums, 0


def binary_search(array, target, left, right):
    if left >= right:
        if target == array[0]:
            return 0
        return -1

    mid = (left + right) // 2

    if target == array[mid]:
        return mid
    else:
        if target < array[mid]:
            return binary_search(array, target, left, mid)
        else:
            return binary_search(array, target, mid + 1, right)


def broken_search(nums, target):
    length = len(nums)
    array, swap_diff = start_search(nums, left=0, right=length - 1)
    print(f'array={array}')

    res = binary_search(array, target, 0, length - 1)

    print(f'array={array}, swap_diff={swap_diff}, res={res}')

    if res == -1:
        return res
    return (res + swap_diff) % length


def test():
    arr = [1, 4, 5, 7, 12, 19, 21, 100, 101]
    assert broken_search(arr, 5) == 6


def main():
    nums, to_find, length = get_input()
    print(f'nums={nums}, to_find={to_find}, length={length}')
    return broken_search(nums, to_find)


if __name__ == '__main__':
    print(main())
