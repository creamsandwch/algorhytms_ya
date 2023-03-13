import sys


def get_input():
    sys.stdin.readline()
    word_list = sys.stdin.readline().strip().split()
    return word_list


def find_first_longest_word(word_list: list):
    longest_word = max(word_list, key=lambda i: len(i))
    sys.stdout.write(str(longest_word) + '\n')
    sys.stdout.write(str(len(longest_word)))


def main():
    find_first_longest_word(get_input())


if __name__ == '__main__':
    main()
