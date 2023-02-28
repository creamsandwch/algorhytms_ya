import sys


def get_input():
    days_count = int(input())
    days_list = list(map(int, sys.stdin.readline().split()))
    days_list.insert(0, -274)
    days_list.append(-274)
    return days_count, days_list


def find_chaotic_weather_days(days_count, daily_temp_list: list):
    if days_count == 1:
        return days_count

    count = 0

    for i in range(1, days_count + 1):
        if (
            daily_temp_list[i - 1] < daily_temp_list[i]
                > daily_temp_list[i + 1]
        ):
            count += 1

    return count


def main():
    print(find_chaotic_weather_days(*get_input()))


if __name__ == '__main__':
    main()
