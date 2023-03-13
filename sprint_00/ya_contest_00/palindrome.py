import sys


def get_input():
    phrase = sys.stdin.readline().strip().lower()

    for char in phrase:
        if not char.isalpha():
            phrase = phrase.replace(char, '')

    return phrase


def check_if_palindrome(phrase: str):
    if phrase == phrase[::-1]:
        return True
    return False


def main():
    sys.stdout.write(str(check_if_palindrome(get_input())))


if __name__ == '__main__':
    main()
