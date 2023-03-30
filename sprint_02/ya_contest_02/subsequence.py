def get_input():
    sub_string = input().strip()
    main_string = input().strip()
    return main_string, sub_string


def is_substring(main_string: str, sub_string: str):
    index = -1
    for char in sub_string:
        print(f'char={char}, main_string[{index}]={main_string[index]}')
        index = main_string.find(char, index + 1)
        if index == -1:
            return False
    return True


def main():
    return is_substring(*get_input())


if __name__ == '__main__':
    print(main())
