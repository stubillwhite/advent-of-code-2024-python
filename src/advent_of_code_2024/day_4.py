from importlib.resources import files
from typing import Dict, Tuple

Grid = Dict[Tuple[int, int], str]


def problem_input() -> str:
    return files("resources").joinpath("day-4-input.txt").read_text()


def _parse_input(s: str) -> Grid:
    return {(x, y): ch for (y, line) in enumerate(s.splitlines()) for (x, ch) in enumerate(line)}


def _xmas_matches(grid: Grid, x: int, y: int) -> int:
    desired_word = "XMAS"

    deltas = [(x, y) for x in range(-1, 2) for y in range(-1, 2)]
    locs = [[(x + (n * dx), (y + (n * dy))) for n in range(len(desired_word))] for (dx, dy) in deltas]
    words = ["".join([grid.get((x, y), "") for (x, y) in loc]) for loc in locs]

    return len([w for w in words if w == desired_word])


def solution_part_one(s: str) -> int:
    grid = _parse_input(s)
    return sum([_xmas_matches(grid, x, y) for (x, y) in grid.keys()])


# Part two


def _x_mas_matches(grid: Grid, x: int, y: int) -> int:

    deltas = [[(-1, -1), (0, 0), (1, 1)], [(1, -1), (0, 0), (-1, 1)]]

    locs = [[(x + dx, y + dy) for (dx, dy) in diagonal] for diagonal in deltas]
    chars = [[grid.get((x, y), "") for (x, y) in diagonal] for diagonal in locs]
    words = ["".join(x) for x in chars]

    return 1 if all([w in ["MAS", "SAM"] for w in words]) else 0


def solution_part_two(s: str) -> int:
    grid = _parse_input(s)
    return sum([_x_mas_matches(grid, x, y) for (x, y) in grid.keys()])


def main() -> None:
    s = problem_input()
    print(solution_part_one(s))
    print(solution_part_two(s))


if __name__ == "__main__":
    main()
