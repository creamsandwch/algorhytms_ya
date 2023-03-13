class StackMax:
    def __init__(self) -> None:
        self.items = []

    def push(self, item):
        print(f'push {item}')
        self.items.append(item)

    def pop(self):
        print('pop')
        return self.items.pop()

    def get_max(self):
        if self.items == []:
            return None
        return max(self.items)


def get_input():
    command_count = input()
    commands = []
    for i in range(len(command_count)):
        commands.append(input().strip())

    return commands


def main():
    commands = get_input()

    stack = StackMax()

    for command in commands:
        print(str(getattr(stack, command)))


if __name__ == '__main__':
    main()
