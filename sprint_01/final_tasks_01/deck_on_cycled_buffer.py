# ID = 84019113


def get_input():
    commands_count = int(input().strip())
    max_deck_size = int(input().strip())

    commands = []

    for i in range(commands_count):
        command = input().strip()
        if 'push' in command:
            command = command.split()
        commands.append(command)

    return max_deck_size, commands


class CycledBufferDeque:
    def __init__(self, max_size: int) -> None:
        self.max_size = max_size
        self.queue = max_size * [None]
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.max_size

    def push_back(self, value):
        if self.is_full():
            return 'error'
        self.tail = (self.tail + 1) % self.max_size
        self.queue[self.tail] = value
        self.size += 1
        return None

    def pop_back(self):
        if self.is_empty():
            return 'error'
        value = self.queue[self.tail]
        self.queue[self.tail] = None
        self.tail = (self.tail - 1) % self.max_size
        self.size -= 1
        return value

    def push_front(self, value):
        if self.is_full():
            return 'error'
        self.queue[self.head] = value
        self.head = (self.head - 1) % self.max_size
        self.size += 1
        return None

    def pop_front(self):
        if self.is_empty():
            return 'error'
        self.head = (self.head + 1) % self.max_size
        value = self.queue[self.head]
        self.queue[self.head] = None
        self.size -= 1
        return value


def main():
    max_deck_size, commands = get_input()
    my_deck = CycledBufferDeque(max_size=max_deck_size)

    for command in commands:
        if type(command) == list:
            output = getattr(my_deck, command[0])(int(command[1]))
            if output is not None:
                print(output)
        else:
            output = getattr(my_deck, command)()
            if output is not None:
                print(output)


if __name__ == '__main__':
    main()
