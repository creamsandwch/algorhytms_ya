class StackMax:
    def __init__(self) -> None:
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items != []:
            return self.items.pop()
        else:
            print('error')

    def get_max(self):
        if self.items == []:
            return None
        return max(self.items)


def get_input():
    command_count = int(input())
    commands = []

    for i in range(command_count):
        command = input().strip()
        if 'push' in command:
            commands.append(command.split())
        else:
            commands.append(command)
    return commands


def main():
    commands = get_input()

    stack = StackMax()

    for command in commands:
        if 'push' in command:
            stack.push(item=int(command[1]))
        elif command == 'get_max':
            print(stack.get_max())
        else:
            stack.pop()


if __name__ == '__main__':
    main()
