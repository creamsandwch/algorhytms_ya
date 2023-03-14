class StackMax:
    def __init__(self) -> None:
        self.items = []
        self.maxes_list = []

    def push(self, item):
        self.items.append(item)

        if self.maxes_list == []:
            self.maxes_list.append(item)
        else:
            if self.maxes_list[-1] <= item:
                self.maxes_list.append(item)

    def pop(self):
        if self.items != []:
            popped_value = self.items.pop()

            if self.maxes_list != [] and popped_value == self.maxes_list[-1]:
                self.maxes_list.pop()
        else:
            print('error')

    def get_max(self):
        if self.maxes_list == []:
            return None
        return self.maxes_list[-1]


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
