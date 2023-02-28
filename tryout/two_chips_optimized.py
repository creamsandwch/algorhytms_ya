def get_input():
    input()
    chips_weight = list(map(int, input().strip().split()))
    lookup_sum = int(input().strip())
    return chips_weight, lookup_sum


def get_lookup_sum_nums(
        chips_weight: list,
        lookup_sum: int
):
    chips_weight.sort()
    left_index = 0
    right_index = len(chips_weight) - 1
    while left_index < right_index:
        sum = chips_weight[left_index] + chips_weight[right_index]
        if sum == lookup_sum:
            return f'{chips_weight[left_index]} {chips_weight[right_index]}'
        elif sum > lookup_sum:
            right_index -= 1
        elif sum < lookup_sum:
            left_index += 1
    return None


def get_lookup_sum_nums_with_set(
        chips_weight: list,
        lookup_sum: int,
):
    previous = set()

    for a in chips_weight:
        if lookup_sum - a in previous:
            return f'{lookup_sum - a} {a}'
        else:
            previous.add(a)

    return None


tuple = get_input()

print(get_lookup_sum_nums(*tuple))
print(get_lookup_sum_nums_with_set(*tuple))
