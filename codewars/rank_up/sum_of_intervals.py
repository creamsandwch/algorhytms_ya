# bro you gotta finish this, feels like we close

def do_intervals_overlap(interval_a, interval_b):
    if (
        interval_a[0] > interval_b[-1]
        or
        interval_a[-1] < interval_b[0]
    ):
        return False
    return True


def sum_of_intervals(intervals: list):
    i = 0
    to_remove = []

    for i in range(len(intervals)):
        for interval in intervals:
            if (
                intervals[i][0] > interval[0]
                and intervals[i][-1] < interval[-1]
            ):
                to_remove.append(intervals[i])

    clean_intervals = []

    for interval in intervals:
        if interval not in to_remove:
            clean_intervals.append(interval)

    result = []

    for i in range(1, len(clean_intervals)):
        check = do_intervals_overlap(
            interval_a=clean_intervals[i - 1],
            interval_b=clean_intervals[i]
        )
        if check:
            result.append((abs(clean_intervals[i - 1][0] - clean_intervals[i][0]), abs(clean_intervals[i - 1][-1] - clean_intervals[i - 1][-1])))
        else:
            result.append(abs(clean_intervals[i][-1] - clean_intervals[i][0]))

    output = 0

    for elem in result:
        if type(elem) == int:
            output += elem
        else:
            output += abs(elem[-1] - elem[0])

    return output


def main():
    intervals = [
        [1, 4],
        [7, 10],
        [3, 5]
    ]

    return sum_of_intervals(intervals)


if __name__ == '__main__':
    print(main())
