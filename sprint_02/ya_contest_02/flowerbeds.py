def get_input():
    count = int(input().strip())
    intervals = []
    for i in range(count):
        start_end = input().strip().split()
        intervals.append([int(start_end[0]), int(start_end[1])])

    return intervals


def intervals_without_overlap(intervals: list):
    intervals.sort()
    output = []

    base_interval = intervals[0]

    for interval in intervals:
        if base_interval[0] <= interval[0] <= base_interval[-1]:
            if base_interval[-1] < interval[-1]:
                base_interval[-1] = interval[-1]
        else:
            output.append(base_interval)

            base_interval = interval
    output.append(base_interval)

    return output


def main():
    intervals = intervals_without_overlap(get_input())

    for elem in intervals:
        print(*elem)


if __name__ == '__main__':
    main()
