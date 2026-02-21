from collections.abc import Callable
from enum import Enum
from pathlib import Path


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


def get_password(input_filepath: Path, increment_func: Callable[..., int]) -> int:
    lines = input_filepath.read_text().splitlines()
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


def count_rotations(position: int, direction: Direction, value: int) -> int:
    increment = 0
    if direction == Direction.LEFT and position != 0:
        increment = ((position - value) * (-1) + DIAL_RANGE) // DIAL_RANGE
    if direction == Direction.LEFT and position == 0:
        increment = ((position - value) * (-1)) // DIAL_RANGE
    if direction == Direction.RIGHT:
        increment = (position + value) // DIAL_RANGE

    # print(f"Increment: {increment}, Position: {position}, Direction: {direction}, Value: {value}")
    return increment


def get_password_of_part_one(input_filepath: Path) -> int:
    return get_password(input_filepath, count_if_position_lands_on_zero)


def get_password_of_part_two(input_filepath: Path) -> int:
    return get_password(input_filepath, count_rotations)


if __name__ == "__main__":
    pass
