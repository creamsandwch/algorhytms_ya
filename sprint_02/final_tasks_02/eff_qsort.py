# 85128893

from typing import Tuple
from dataclasses import dataclass


@dataclass
class Student:
    name: str
    score: int
    penalties: int

    def params(self):
        return (-self.score, self.penalties, self.name)

    def __str__(self):
        return self.name


def qsort_in_place(array: list, init_left: int, init_right: int) -> None:
    if init_left >= init_right:
        return

    left, right = init_left, init_right

    pivot = array[(init_left + init_right) // 2]

    while left <= right:
        while array[left].params() > pivot.params():
            left += 1
        while array[right].params() < pivot.params():
            right -= 1

        if left <= right:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1

    qsort_in_place(array, init_left, right)
    qsort_in_place(array, left, init_right)


def get_input() -> Tuple[int, list]:
    length = int(input().strip())
    contestants = []
    for i in range(length):
        name, score, penalties = input().strip().split()
        contestants.append(Student(name, int(score), int(penalties)))

    return length, contestants


def main() -> None:
    length, array = get_input()

    qsort_in_place(array, 0, length - 1)

    for elem in array[::-1]:
        print(elem)


if __name__ == '__main__':
    main()
