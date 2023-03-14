def is_bracket_sequence_legit(sequence: list):
    stack = []
    left_brackets = ['(', '[', '{']
    right_brackets = [')', ']', '}']

    for elem in sequence:
        if elem in left_brackets:
            stack.append(elem)
        elif (
            elem in right_brackets and stack == []
            or
            (
                elem in right_brackets
                and left_brackets.index(stack[-1])
                != right_brackets.index(elem)
            )
        ):
            return False
        else:
            del stack[-1]
    if stack != []:
        return False
    return True


def main():
    print(is_bracket_sequence_legit([*input().strip()]))


if __name__ == '__main__':
    main()
