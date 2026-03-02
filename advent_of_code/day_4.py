from pathlib import Path

from utils.day import Day
from utils.io_actions import read_lines


class DayFour(Day):
    def __init__(self):
        super().__init__(number=4)

    def solve_part_one(self, input_filepath: Path | str) -> int:
        return get_password(input_filepath)

    def solve_part_two(self, input_filepath: Path | str) -> int:
        return get_password(input_filepath)


def get_password(input_filepath: Path | str) -> int:
    pass