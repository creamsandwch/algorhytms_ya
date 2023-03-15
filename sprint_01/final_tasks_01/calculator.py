# ID = 84023350


import operator


OPERATORS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv,
}


def main():
    line = input().strip().split()

    stack = []

    for elem in line:
        if elem not in OPERATORS:
            stack.append(int(elem))
        else:
            value_1 = stack.pop()
            value_2 = stack.pop()
            stack.append(OPERATORS[elem](value_2, value_1))

    print(stack.pop())


if __name__ == '__main__':
    main()
