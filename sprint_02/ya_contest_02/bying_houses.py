def get_input():
    budget = int(input().strip().split()[1])
    prices_list = list(map(int, input().strip().split()))
    return budget, prices_list


def get_max_amount_of_houses(budget: int, prices_list: list):
    prices_list.sort()

    to_pay = 0
    count = 0

    for elem in prices_list:
        if to_pay + elem > budget:
            break
        else:
            to_pay += elem
            count += 1

    return count


def main():
    print(get_max_amount_of_houses(*get_input()))


if __name__ == '__main__':
    main()
