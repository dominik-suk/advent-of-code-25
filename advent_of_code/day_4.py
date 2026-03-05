import copy
from enum import Enum
from pathlib import Path
from typing import Callable

from utils.day import Day
from utils.io_actions import read_lines


class DayFour(Day):
    def __init__(self):
        super().__init__(number=4)

    def solve_part_one(self, input_filepath: Path | str) -> int:
        return get_password(input_filepath, count_currently_accessible_rolls)

    def solve_part_two(self, input_filepath: Path | str) -> int:
        return get_password(input_filepath, count_all_accessible_rolls)


class Symbols(Enum):
    PAPER_ROLL = '@'
    EMPTY_SPACE = '.'


def lines_to_2d_array(lines: list[str]) -> list[list[str]]:
    return [list(line) for line in lines]


def count_neighbors(grid: list[list[str]], tile: tuple[int, int]) -> int:
    neighbors = 0
    for row in range(max(tile[0] - 1, 0), min(tile[0] + 2, len(grid))):
        for col in range(max(tile[1] - 1, 0), min(tile[1] + 2, len(grid[row]))):
            if row == tile[0] and col == tile[1]:
                continue
            if grid[row][col] == Symbols.PAPER_ROLL.value:
                neighbors += 1
    return neighbors


def get_modified_grid_and_accessible_rolls_count(grid: list[list[str]]) -> tuple[list[list[str]], int]:
    new_grid = copy.deepcopy(grid)
    accessible_rolls = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if tile_is_occupied(grid, tile=(row, col)) and roll_is_accessible(grid, tile=(row, col)):
                accessible_rolls += 1
                new_grid[row][col] = Symbols.EMPTY_SPACE.value
    return new_grid, accessible_rolls


def tile_is_occupied(grid: list[list[str]], tile: tuple[int, int]) -> bool:
    row, col = tile[0], tile[1]
    return grid[row][col] != Symbols.EMPTY_SPACE.value


def roll_is_accessible(grid: list[list[str]], tile: tuple[int, int]) -> bool:
    return count_neighbors(grid, tile) < 4


def count_currently_accessible_rolls(grid: list[list[str]]) -> int:
    return get_modified_grid_and_accessible_rolls_count(grid)[1]


def count_all_accessible_rolls(grid: list[list[str]]) -> int:
    all_accessible_rolls = 0
    end_reached = False
    current_grid = copy.deepcopy(grid)
    while not end_reached:
        modified_grid, current_accessible_rolls = get_modified_grid_and_accessible_rolls_count(current_grid)
        if modified_grid == current_grid:
            end_reached = True
        else:
            all_accessible_rolls += current_accessible_rolls
            current_grid = modified_grid
    return all_accessible_rolls


def get_password(input_filepath: Path | str, count_rolls: Callable[[list[list[str]]], int]) -> int:
    lines = read_lines(input_filepath)
    grid = lines_to_2d_array(lines)
    accessible_rolls = count_rolls(grid)

    return accessible_rolls
