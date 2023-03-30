def start_search(nums, left, right):
    if right - left <= 1:
        return right

    mid = (left + right) // 2

    if nums[mid] < nums[mid - 1]:
        return mid
    else:
        start_search(nums, left, mid)
        start_search(nums, mid + 1, right)
    return right


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


def broken_search(nums, target) -> int:
    mid = start_search(nums, 0, len(nums) - 1)

    if nums[mid] == target:
        return mid

    if nums[mid] < nums[mid - 1]:
        nums = nums[mid:] + nums[:mid]
        swap_diff = len(nums[mid:])
    else:
        swap_diff = 0

    res = binary_search(nums, target, 0, len(nums) - 1)

    if res == -1:
        return res

    return (res - swap_diff) % (len(nums))
