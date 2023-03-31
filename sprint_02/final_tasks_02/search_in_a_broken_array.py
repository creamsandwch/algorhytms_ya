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


def broken_binary_search(nums, target, left, right, divider=None):
    mid = (left + right) // 2

    print(f'mid={nums[mid]}, {nums[mid - 1]}')

    if nums[mid] == target:
        return mid
    elif right - left <= 1:
        if nums[left] == target:
            return left
        return -1
    else:
        if nums[mid] < nums[mid - 1]:
            divider = mid

            if nums[divider] <= target <= nums[right - 1]:
                return binary_search(nums, target, divider, right)
            elif nums[left] <= target <= nums[divider - 1]:
                return binary_search(nums, target, left, divider)
            else:
                return -1
        else:
            if divider is None:
                broken_binary_search(nums, target, left, mid)
                broken_binary_search(nums, target, mid, right)
            return binary_search(nums, target, 0, right)


def start_finder(array, left, right):

    while left <= right:
        mid = (left + right) // 2

        if array[mid] >= array[right]:
            left = mid + 1
        else:
            right = mid

    return mid


def broken_search(nums, target):
    mid = start_finder(nums, 0, len(nums) - 1)

    if target == nums[mid]:
        return mid
    elif target >= nums[mid]:
        return binary_search(nums, target, mid, len(nums) - 1)
    else:
        return binary_search(nums, target, 0, mid)
