from pathlib import Path


def read_lines(path: Path | str) -> list[str]:
    if isinstance(path, str):
        path = Path(path)
    return path.read_text().splitlines()
