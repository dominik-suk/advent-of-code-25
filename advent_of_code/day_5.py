import copy
from pathlib import Path
from typing import Callable

from utils.day import Day
from utils.io_actions import read_lines


class DayFive(Day):
    def __init__(self):
        super().__init__(number=5)

    def solve_part_one(self, input_filepath: Path | str) -> int:
        return get_password(input_filepath, count_fresh_ingredients_from_list)

    def solve_part_two(self, input_filepath: Path | str) -> int:
        return get_password(input_filepath, count_all_fresh_ingredients)


def split_in_two_on_blank(lines: list[str]) -> tuple[list[str], list[str]]:
    for i in range(len(lines)):
        if lines[i].strip() == "":
            return lines[:i], lines[i+1:]
    raise ValueError("No Empty line found")


def get_ids(ids_str: list[str]) -> list[int]:
    return [int(_id) for _id in ids_str]


def get_ranges(ranges_str: list[str]) -> list[tuple[int, int]]:
    return [(int(range_str.split("-")[0]), int(range_str.split("-")[1])) for range_str in ranges_str]


def get_min_id(ranges: list[tuple[int, int]]) -> int:
    return min(ranges, key=lambda x: x[0])[0]


def get_max_id(ranges: list[tuple[int, int]]) -> int:
    return max(ranges, key=lambda x: x[1])[1]


def squish_iteration(ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    new_ranges = []
    for i in range(len(ranges)):
        min_i, max_i = ranges[i]
        for j in range(len(ranges)):
            min_j, max_j = ranges[j]
            if i == j:
                continue
            elif min_i <= min_j <= max_j <= max_i:
                _range = (min_i, max_i)
                if _range not in new_ranges:
                    new_ranges.append(_range)
                break
            elif min_i <= min_j <= max_i <= max_j:
                _range = (min_i, max_j)
                if _range not in new_ranges:
                    new_ranges.append(_range)
                break
            elif min_j <= min_i <= max_j <= max_i:
                _range = (min_j, max_i)
                if _range not in new_ranges:
                    new_ranges.append(_range)
                break
            elif min_j <= min_i <= max_i <= max_j:
                _range = (min_j, max_j)
                if _range not in new_ranges:
                    new_ranges.append(_range)
                break
        else:
            new_ranges.append((min_i, max_i))
    return new_ranges


def squish(ranges):
    ranges_copy = copy.deepcopy(ranges)
    end_reached = False
    while not end_reached:
        new_ranges = squish_iteration(ranges_copy)
        if ranges_copy == new_ranges:
            end_reached = True
        else:
            ranges_copy = new_ranges
    return ranges_copy


def count_fresh_ingredients_from_list(ranges: list[tuple[int, int]], ids: list[int]):
    number_of_fresh_ingredients = 0
    for _id in ids:
        for _range in ranges:
            if _range[0] <= _id <= _range[1]:
                number_of_fresh_ingredients += 1
                break
    return number_of_fresh_ingredients


def count_all_fresh_ingredients(ranges: list[tuple[int, int]], _):
    number_of_fresh_ingredients = 0
    for _range in ranges:
        number_of_fresh_ingredients += _range[1] - _range[0] + 1
    return number_of_fresh_ingredients


def get_password(input_filepath: Path | str, ingredients_counter_func: Callable[[list[tuple[int, int]], list[int]], int]) -> int:
    lines = read_lines(input_filepath)
    ranges_str, ids_str = split_in_two_on_blank(lines)
    ranges = squish(get_ranges(ranges_str))
    ids = get_ids(ids_str)

    return ingredients_counter_func(ranges, ids)
