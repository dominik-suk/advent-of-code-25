from abc import ABC, abstractmethod
from pathlib import Path

from utils.io_actions import measure_latency_of_function, measure_average_latency_of_function


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
        print("Sample Input")
        print("Day {}".format(self.number))
        print("Part 1 Password: {}".format(self.solve_part_one(self.sample_filepath)))
        print("Part 2 Password: {}".format(self.solve_part_two(self.sample_filepath)), end="\n\n")

    def run_and_measure_time(self):
        print("Day {}".format(self.number))
        password, time_taken = measure_latency_of_function(self.solve_part_one, self.input_filepath)
        print("Part 1 Password: {}, Time taken: {} seconds".format(password, time_taken), end="\n\n")
        password, time_taken = measure_latency_of_function(self.solve_part_two, self.input_filepath)
        print("Part 2 Password: {}, Time taken: {} seconds".format(password, time_taken), end="\n\n")

    def measure_average_time(self, n: int = 100):
        print("Day {}".format(self.number))
        time_taken = measure_average_latency_of_function(self.solve_part_one, self.input_filepath, n=n)
        print("Time taken for part 1: {} seconds".format(time_taken), end="\n\n")
        time_taken = measure_average_latency_of_function(self.solve_part_two, self.input_filepath, n=n)
        print("Time taken for part 2: {} seconds".format(time_taken), end="\n\n")