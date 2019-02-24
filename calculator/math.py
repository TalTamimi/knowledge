from enum import Enum

from calender.months import Event


def sum(first_number: int, second_number: int) -> int:
    return first_number + second_number


sum('t', 'b')
event = Event()
event.is_event()
print(event.print_day())


class Season(Enum):
    Winter = (0, 3)
    SPRING = (4, 7)
    SUMMER = (8, 11)
    FALL = (11, 17)


    def __init__(self, start, end):
        self.start = start
        self.end = end

    def is_within(self, month: int):
        return self.start > month & self.end < month


Season.SUMMER.is_within(5)


def clustering(kernel: Season):
    return 1


clustering(Season.EXPONENTIAL)
