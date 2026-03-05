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


def get_max_joltage_from_line(line: str, batteries_to_turn_on_per_bank: int) -> int:
    batteries = line_to_array(line)
    max_joltage = ""
    current_index = -1

    for current_battery_number in range(1, batteries_to_turn_on_per_bank + 1):
        number_of_batteries_left_to_turn_on = len(batteries) - batteries_to_turn_on_per_bank + current_battery_number
        batteries_left = batteries[current_index + 1 : number_of_batteries_left_to_turn_on]
        battery_index, battery = get_index_and_max(batteries_left)
        current_index += battery_index + 1
        max_joltage += str(battery)

    return int(max_joltage)


def get_index_and_max(line: list[int]) -> tuple[int, int]:
    return max(enumerate(line), key=lambda x: x[1])


def line_to_array(line: str) -> list:
    return [int(c) for c in line]


def get_password(input_filepath: Path | str, batteries_per_bank: int) -> int:
    lines = read_lines(input_filepath)
    total_joltage = 0
    for line in lines:
        max_joltage = get_max_joltage_from_line(line, batteries_per_bank)
        total_joltage += max_joltage
    return total_joltage
