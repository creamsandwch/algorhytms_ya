def get_input():
    seconds = int(input().strip())
    requests_num_list = list(map(int, input().strip().split()))
    sliding_window_len = int(input().strip())
    return seconds, requests_num_list, sliding_window_len


def sliding_average(seconds: int, requests_num: list, window_len: int):
    result = []
    current_sum = sum(requests_num[0:window_len])
    print(current_sum / window_len, end=' ')
    result.append(current_sum / window_len)
    for i in range(seconds - window_len):
        current_sum = (
            current_sum - requests_num[i] + requests_num[i + window_len]
        )
        current_avg = current_sum / window_len
        result.append(current_avg)
        print(current_avg, end=' ')
    return result


n, q, k = get_input()

sliding_average(n, q, k)
