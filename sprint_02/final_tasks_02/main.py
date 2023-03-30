from search_in_a_broken_array import broken_search


def main():
    length = int(input().strip())
    target = int(input().strip())
    nums = list(map(int, input().strip().split()))

    print(broken_search(nums, target))


if __name__ == '__main__':
    main()
