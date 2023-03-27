def get_input():
    days = int(input())
    money_on_days = [int(x) for x in input().strip().split()]
    bike_cost = int(input().strip())
    return days, money_on_days, bike_cost


def find_days_to_buy_bikes(money: list, bike_cost: int, left, right):
    if right <= left and left != 0:
        return -1

    mid = (left + right) // 2

    if money[mid] >= bike_cost and (money[mid - 1] < bike_cost or mid == 0):
        return mid + 1
    elif money[mid] < bike_cost:
        return find_days_to_buy_bikes(money, bike_cost, mid + 1, right)
    else:
        return find_days_to_buy_bikes(money, bike_cost, left, mid)


def main():
    days, money, bike_cost = get_input()
    if money[-1] < bike_cost:
        return -1, -1
    if money[-1] < bike_cost * 2:
        one_bike = find_days_to_buy_bikes(money, bike_cost, 0, len(money))
        return one_bike, -1
    else:
        one_bike = find_days_to_buy_bikes(money, bike_cost, 0, len(money))
        two_bikes = find_days_to_buy_bikes(money, bike_cost * 2, 0, len(money))
    return one_bike, two_bikes


if __name__ == '__main__':
    print(*main())
