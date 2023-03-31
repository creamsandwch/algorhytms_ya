from broken_search import broken_search, binary_search


def old_broken_search(nums, target) -> int:
    mid = broken_search(nums, target, 0, len(nums) - 1)

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


def main():
    input()
    target = int(input().strip())
    nums = list(map(int, input().strip().split()))

    print(broken_search(nums, target))

    print(f'check = {target in nums}')


if __name__ == '__main__':
    main()
