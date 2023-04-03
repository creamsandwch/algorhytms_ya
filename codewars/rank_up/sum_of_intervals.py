# bro you gotta finish this, feels like we close

def do_intervals_overlap(interval_a, interval_b):
    if (
        interval_a[0] <= interval_b[-1]
        or
        interval_a[-1] >= interval_b[0]
    ):
        return False
    return True


def get_interval_length(interval):
    start, end = interval[0], interval[-1]
    if start >= 0 and end > 0:
        return end - start
    elif start <= 0 and end > 0:
        return abs(start) + end
    elif start < 0 and end < 0:
        return abs(start) - abs(end)
    else:
        return abs(end) + start


def sum_of_intervals(intervals: list):
    i = 0
    to_remove = []

    for i in range(len(intervals)):
        for interval in intervals:
            if intervals.index(interval) != i:
                if (
                    intervals[i][0] >= interval[0]
                    and intervals[i][-1] <= interval[-1]
                ):
                    to_remove.append(intervals[i])

    clean_intervals = []

    for interval in intervals:
        if interval not in to_remove:
            clean_intervals.append(interval)

    result = []

    print(f'to_remove = {to_remove}, clean_intervals = {clean_intervals}')

    for interval in clean_intervals:
        print(f'interval {interval} length = {get_interval_length(interval)}')

    for i in range(1, len(clean_intervals)):
        check = do_intervals_overlap(
            interval_a=clean_intervals[i - 1],
            interval_b=clean_intervals[i]
        )
        if check:
            if clean_intervals[i - 1][0] <= clean_intervals[i][0]:
                clean_intervals[i][0] = clean_intervals[i - 1][0]
            elif clean_intervals[i - 1][-1] >= clean_intervals[i][-1]:
                clean_intervals[i][-1] = clean_intervals[i - 1][-1]

        print(f'clean_intervals[i] = {clean_intervals[i]}')
        result.append(clean_intervals[i][-1] - clean_intervals[i][0])

    print(f'clean_intervals={clean_intervals}, result={result}')

    return sum(result)


def main():
    intervals = [
        [1, 5],
        [10, 20],
        [1, 6],
        [16, 19],
        [5, 11]
    ]

    return sum_of_intervals(intervals)


if __name__ == '__main__':
    print(main())
