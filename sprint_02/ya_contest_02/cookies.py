def get_input():
    input()
    greed_factor = list(map(int, input().strip().split()))
    input()
    cookies_size = list(map(int, input().strip().split()))
    return greed_factor, cookies_size


def count_of_satisfied(greeds: list, cookies: list):
    res = 0
    greeds.sort()
    cookies.sort()
    greed_idx, cookie_idx = 0, 0

    while greed_idx < len(greeds) and cookie_idx < len(cookies):
        if greeds[greed_idx] > cookies[cookie_idx]:
            cookie_idx += 1
        else:
            res += 1
            greed_idx += 1
            cookie_idx += 1

    return res


def main():
    greed_factor, cookies_size = get_input()

    res = count_of_satisfied(greed_factor, cookies_size)

    return res


if __name__ == '__main__':
    print(main())
