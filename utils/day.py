from abc import ABC, abstractmethod
from pathlib import Path


class Day(ABC):
    def __init__(self, number: int, input_filename: Path | str) -> None:
        self.number: int = number
        self.input_filename: Path | str = input_filename

    @abstractmethod
    def solve_part_one(self, input_filename: Path | str) -> str:
        pass

    @abstractmethod
    def solve_part_two(self, input_filename: Path | str) -> str:
        pass

    def run(self):
        print("Day {}".format(self.number))
        print("Part 1 Password: {}".format(self.solve_part_one(self.input_filename)))
        print("Part 2 Password: {}".format(self.solve_part_two(self.input_filename)), end="\n\n")
