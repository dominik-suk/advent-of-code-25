from collections.abc import Callable
from enum import Enum
from pathlib import Path

from utils.io_actions import read_lines
from utils.day import Day


class DayOne(Day):
    def __init__(self):
        super().__init__(number=1)

    def solve_part_one(self, input_filepath: Path | str) -> int:
        return get_password(input_filepath, count_if_position_lands_on_zero)

    def solve_part_two(self, input_filepath: Path | str) -> int:
        return get_password(input_filepath, count_if_position_crosses_zero)


STARTING_POSITION: int = 50
DIAL_RANGE: int = 100


class Direction(Enum):
    LEFT = "L"
    RIGHT = "R"


def get_position_after_rotation(current_position: int, direction: Direction, value: int) -> int:
    if direction == Direction.LEFT:
        return (current_position - value) % DIAL_RANGE
    return (current_position + value) % DIAL_RANGE


def parse_line(line: str) -> tuple[Direction, int]:
    direction = Direction(line[0])
    value = int(line[1:])
    return direction, value


def get_password(input_filepath: Path | str, increment_func: Callable[..., int]) -> int:
    lines = read_lines(input_filepath)
    position = STARTING_POSITION
    counter = 0
    for line in lines:
        direction, value = parse_line(line)
        previous_position = position
        position = get_position_after_rotation(position, direction, value)
        counter += increment_func(previous_position, direction, value)

    return counter


def count_if_position_lands_on_zero(position: int, *_) -> int:
    if position == 0:
        return 1
    return 0


def count_if_position_crosses_zero(position: int, direction: Direction, value: int) -> int:
    if direction == Direction.LEFT:
        if position == 0:
            return -(position - value) // DIAL_RANGE
        else:
            return -(position - value) // DIAL_RANGE + 1
    else:
        return (position + value) // DIAL_RANGE
