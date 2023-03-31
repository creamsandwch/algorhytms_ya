# 84888806


def binary_search(array, target, left, right):
    if left >= right:
        return -1

    mid = (left + right) // 2

    if target == array[mid]:
        return mid
    else:
        if target < array[mid]:
            return binary_search(array, target, left, mid)
        else:
            return binary_search(array, target, mid + 1, right)


def start_finder(array):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left + right) // 2

        if array[mid] >= array[right]:
            left = mid + 1
        else:
            right = mid

    return mid


def broken_search(nums, target):
    mid = start_finder(nums)
    left = 0
    right = len(nums) - 1

    if target == nums[mid]:
        return mid
    elif nums[mid] <= target <= nums[right]:
        return binary_search(nums, target, mid, len(nums))
    else:
        return binary_search(nums, target, left, mid)
