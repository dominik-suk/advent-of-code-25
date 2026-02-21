from abc import ABC, abstractmethod
from pathlib import Path


class Day(ABC):
    def __init__(self, number: int) -> None:
        self.number: int = number
        self.input_filepath: Path | str = "advent_of_code/docs/day-{}/input.txt".format(self.number)
        self.sample_filepath: Path | str = "advent_of_code/docs/day-{}/sample.txt".format(self.number)

    @abstractmethod
    def solve_part_one(self, input_filename: Path | str) -> str:
        pass

    @abstractmethod
    def solve_part_two(self, input_filename: Path | str) -> str:
        pass

    def run(self):
        print("Day {}".format(self.number))
        print("Part 1 Password: {}".format(self.solve_part_one(self.input_filepath)))
        print("Part 2 Password: {}".format(self.solve_part_two(self.input_filepath)), end="\n\n")

    def run_sample(self):
        print("Day {}".format(self.number))
        print("Part 1 Password: {}".format(self.solve_part_one(self.sample_filepath)))
        print("Part 2 Password: {}".format(self.solve_part_two(self.sample_filepath)), end="\n\n")