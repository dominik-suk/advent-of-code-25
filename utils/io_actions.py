import time
from pathlib import Path
from typing import Callable, Any


def read_lines(path: Path | str) -> list[str]:
    if isinstance(path, str):
        path = Path(path)
    return path.read_text().splitlines()


def read_list(path: Path | str) -> list[str]:
    if isinstance(path, str):
        path = Path(path)
    return path.read_text().split(',')


def measure_latency_of_function(func: Callable, *args, **kwargs) -> tuple[Any, float]:
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    time_taken = round(end_time - start_time, 2)

    return result, time_taken


def measure_average_latency_of_function(func: Callable, *args, n=100, **kwargs) -> float:
    sum_of_times = 0.0
    for i in range(n):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        time_taken = round(end_time - start_time, 2)
        sum_of_times += time_taken
    return round(sum_of_times / n, 2)