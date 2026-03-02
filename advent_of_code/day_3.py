from pathlib import Path

from utils.day import Day
from utils.io_actions import read_lines


class DayThree(Day):
    def __init__(self):
        super().__init__(number=3)

    def solve_part_one(self, input_filepath: Path | str) -> int:
        return get_password(input_filepath, batteries_per_bank=2)

    def solve_part_two(self, input_filepath: Path | str) -> int:
        return get_password(input_filepath, batteries_per_bank=12)


def get_max_joltage_from_line(line: str, batteries_per_bank) -> int:
    batteries = line_to_array(line)
    max_joltage = ""
    current_index = -1

    for i in range(batteries_per_bank):
        batteries_left = batteries[current_index + 1 : len(batteries) - (batteries_per_bank - (i + 1))]
        battery, partial_index = get_max_and_index(batteries_left)
        current_index += partial_index + 1
        max_joltage += str(battery)

    return int(max_joltage)


def get_max_and_index(line: list[int]) -> tuple[int, int]:
    index = 0
    highest_value = line[0]
    for number in range(0, len(line)):
        if line[number] > highest_value:
            highest_value = line[number]
            index = number

    return highest_value, index


def line_to_array(line: str) -> list:
    arr = []
    for char in line:
        arr.append(int(char))
    return arr


def get_password(input_filepath: Path | str, batteries_per_bank) -> int:
    lines = read_lines(input_filepath)
    total_joltage = 0
    for line in lines:
        max_joltage = get_max_joltage_from_line(line, batteries_per_bank)
        total_joltage += max_joltage
    return total_joltage
