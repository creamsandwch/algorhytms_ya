def get_commits_count(workers_count: int, last_num_count, stack=[1, 1]):
    dec_divider = 10 ** last_num_count

    a = 1
    b = 1

    ops_count = 0

    for i in range(2, workers_count + 1):
        a, b = (b % dec_divider), (b % dec_divider + a % dec_divider)
        ops_count += 1

    return b % dec_divider


def main():
    input_list = input().strip().split()
    workers_count = int(input_list[0])
    last_num_count = int(input_list[1])
    print(get_commits_count(workers_count, last_num_count))


if __name__ == '__main__':
    main()
