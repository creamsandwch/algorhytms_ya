def filter_list(unfiltered_list: list):
    filtered_list = list(
        filter(
            lambda x: (type(x) == int),
            unfiltered_list
        )
    )
    return filtered_list


def main():
    print(filter_list([1, 2, 'a', 'b']))
    print(filter_list([1, 2, 'aasf', '1', '123', 123, 0]))


if __name__ == '__main__':
    main()
