from typing import Callable

from utils.io_actions import read_list

from pathlib import Path
from utils.day import Day

class DayTwo(Day):
    def __init__(self):
        super().__init__(number=2)

    def solve_part_one(self, input_filepath: Path | str) -> int:
        return get_password(input_filepath, id_is_repeated_twice)

    def solve_part_two(self, input_filepath: Path | str) -> int:
        return get_password(input_filepath, id_is_repeated_at_least_twice)


def parse_segment(segment) -> tuple[int, int]:
    id_range = segment.split('-')
    first_id = int(id_range[0])
    last_id = int(id_range[1])
    return first_id, last_id


def id_is_valid(product_id: int, found_sequence_func: Callable[[int], bool]) -> bool:
    if id_has_leading_zero(product_id):
        return False
    if found_sequence_func(product_id):
        return False
    return True


def id_has_odd_length(product_id: int) -> bool:
    return len(str(product_id)) % 2 != 0


def id_has_leading_zero(product_id: int) -> bool:
    return str(product_id).startswith('0')


def id_is_repeated_twice(product_id: int) -> bool:
    if id_has_odd_length(product_id):
        return False
    product_id = str(product_id)
    first_half = product_id[:len(product_id) // 2]
    second_half = product_id[len(product_id) // 2:]
    return first_half == second_half


def id_is_repeated_at_least_twice(product_id: int) -> bool:
    product_id = str(product_id)
    sequence = product_id[0]
    for digit in product_id[1:]:
        if digit == sequence[0] and sequence_is_repeating(product_id, sequence):
            return True
        sequence += digit
    return False


def sequence_is_repeating(product_id: str, sequence: str) -> bool:
    found_sequence = True
    for i in range(len(product_id)):
        if len(product_id) % len(sequence) != 0:
            found_sequence = False
            break
        if product_id[i] != sequence[i % len(sequence)]:
            found_sequence = False
            break
    return found_sequence


def get_password(input_filepath: Path | str, found_sequence_func: Callable[[int], bool]) -> int:
    segments = read_list(input_filepath)
    password = 0
    for segment in segments:
        first_id, last_id = parse_segment(segment)
        for product_id in range(first_id, last_id + 1):
            if not id_is_valid(product_id, found_sequence_func):
                password += product_id
    return password
