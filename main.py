from pathlib import Path
from advent_of_code import day_1


def print_day_1():
    input_filepath = Path("advent_of_code/docs/day-1/input.txt")
    password_part_one = day_1.get_password_of_part_one(input_filepath)
    password_part_two = day_1.get_password_of_part_two(input_filepath)

    print("Day 1")
    print(f"Part 1 Password: {password_part_one}")
    print(f"Part 2 Password: {password_part_two}", end="\n\n")

if __name__ == "__main__":
    print_day_1()
