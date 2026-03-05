import json
import pytest
from pathlib import Path

from advent_of_code import *


class TestSolve:
    @pytest.fixture
    def solutions(self):
        with open(Path(__file__).parent / "solutions.json") as solutions_file:
            solutions_dict = json.load(solutions_file)
        return solutions_dict

    def test_day_one(self, solutions):
        result = DayOne().solve()
        assert result["part 1"]["sample"] == solutions["day 1"]["part 1"]["sample"]
        assert result["part 2"]["sample"] == solutions["day 1"]["part 2"]["sample"]
        assert result["part 1"]["input"]  == solutions["day 1"]["part 1"]["input"]
        assert result["part 2"]["input"]  == solutions["day 1"]["part 2"]["input"]

    def test_day_two(self, solutions):
        result = DayTwo().solve()
        assert result["part 1"]["sample"] == solutions["day 2"]["part 1"]["sample"]
        assert result["part 2"]["sample"] == solutions["day 2"]["part 2"]["sample"]
        assert result["part 1"]["input"]  == solutions["day 2"]["part 1"]["input"]
        assert result["part 2"]["input"]  == solutions["day 2"]["part 2"]["input"]

    def test_day_three(self, solutions):
        result = DayThree().solve()
        assert result["part 1"]["sample"] == solutions["day 3"]["part 1"]["sample"]
        assert result["part 2"]["sample"] == solutions["day 3"]["part 2"]["sample"]
        assert result["part 1"]["input"]  == solutions["day 3"]["part 1"]["input"]
        assert result["part 2"]["input"]  == solutions["day 3"]["part 2"]["input"]

    def test_day_four(self, solutions):
        result = DayFour().solve()
        assert result["part 1"]["sample"] == solutions["day 4"]["part 1"]["sample"]
        assert result["part 2"]["sample"] == solutions["day 4"]["part 2"]["sample"]
        assert result["part 1"]["input"]  == solutions["day 4"]["part 1"]["input"]
        assert result["part 2"]["input"]  == solutions["day 4"]["part 2"]["input"]
