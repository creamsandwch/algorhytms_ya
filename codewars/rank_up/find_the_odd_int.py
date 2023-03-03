def find_it(seq: list) -> int:
    seq_set = set(seq)
    seq_list = list(seq_set)
    seq_list.sort
    for i in seq_list:
        if seq.count(i) % 2 == 0:
            return i


def main():
    print(find_it([7]))
    print(find_it([1, 1, 2]))
    print(find_it([1, 2, 2, 3, 3, 3, 4, 3, 3, 3, 2, 2, 1]))
    print('XOR')
    a = 2
    b = 3
    print(f'2 ^ 3 = {a ^ b}')


if __name__ == '__main__':
    main()
