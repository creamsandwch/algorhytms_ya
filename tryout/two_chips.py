def get_input():
    chips_count = int(input().strip())
    chips_weight = list(map(int, input().strip().split()))
    lookup_sum = int(input().strip())
    return chips_count, chips_weight, lookup_sum


def get_lookup_sum_nums(chips_count: int, chips_weight: list, lookup_sum: int):
    for i in range(chips_count):
        for j in range(i + 1, chips_count):
            if chips_weight[i] + chips_weight[j] == lookup_sum:
                return f'{chips_weight[i]} {chips_weight[j]}'

    return None


print(get_lookup_sum_nums(*get_input()))
