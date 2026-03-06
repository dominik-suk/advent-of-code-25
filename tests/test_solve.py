import json
import functools
import pytest
from pathlib import Path

from advent_of_code import (
    DayOne, DayTwo, DayThree, DayFour, DayFive, DaySix,
    DaySeven, DayEight, DayNine, DayTen, DayEleven, DayTwelve,
)

DAYS = [
    ("day 1",  DayOne),
    ("day 2",  DayTwo),
    ("day 3",  DayThree),
    ("day 4",  DayFour),
    ("day 5",  DayFive),
    ("day 6",  DaySix),
    ("day 7",  DaySeven),
    ("day 8",  DayEight),
    ("day 9",  DayNine),
    ("day 10", DayTen),
    ("day 11", DayEleven),
    ("day 12", DayTwelve),
]

CASES = [
    pytest.param(key, cls, part, split, id=f"{key}-{part}-{split}")
    for key, cls in DAYS
    for part in ["part 1", "part 2"]
    for split in ["sample", "input"]
]


@functools.lru_cache(maxsize=None)
def _solve(cls):
    return cls().solve()


class TestSolve:
    @pytest.fixture(scope="class")
    def solutions(self):
        with open(Path(__file__).parent / "solutions.json") as solutions_file:
            return json.load(solutions_file)

    @pytest.mark.parametrize("key,cls,part,split", CASES)
    def test_day(self, key, cls, part, split, solutions):
        assert _solve(cls)[part][split] == solutions[key][part][split]