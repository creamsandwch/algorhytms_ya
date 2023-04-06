def get_input():
    input()
    sides_lens = list(map(int, input().strip().split()))
    return sides_lens


def max_triangle_perimeter(sides_length: list):
    sides_length.sort(reverse=True)
    for i in range(len(sides_length) - 2):
        if sides_length[i] < sides_length[i + 1] + sides_length[i + 2]:
            return sum(sides_length[i:i+3])
    return 'kek'


def main():
    print(max_triangle_perimeter(get_input()))


if __name__ == '__main__':
    main()
