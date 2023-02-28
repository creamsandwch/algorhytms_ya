import sys


def get_input():
    sys.stdin.readline()
    word_list = sys.stdin.readline().strip().split()
    return word_list


def find_first_longest_word(word_list: list):
    base_length = 0
    for word in word_list:
        length = len(word)
        if length > base_length:
            longest_word = word
            base_length = length

    sys.stdout.write(str(longest_word) + '\n')
    sys.stdout.write(str(base_length))


def main():
    find_first_longest_word(get_input())


if __name__ == '__main__':
    main()
