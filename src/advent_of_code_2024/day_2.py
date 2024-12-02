from importlib.resources import read_text
from typing import Generator, Sequence


def problem_input() -> str:
    return read_text("resources", "day-2-input.txt")


def parse_input(s: str) -> list[list[int]]:
    return [[int(x) for x in line.split()] for line in s.splitlines()]


def _sliding[A](xs: Sequence[A], n: int) -> Generator[None, None, Sequence[A]]:
    for i in range(len(xs) - n + 1):
        yield xs[i : i + n]


def _is_safe(xs: list[int]) -> bool:
    all_increasing = all([a < b for a, b in _sliding(xs, 2)])
    all_decreasing = all([a > b for a, b in _sliding(xs, 2)])
    small_deltas = all([1 <= abs(a - b) <= 3 for a, b in _sliding(xs, 2)])
    return (all_increasing or all_decreasing) and small_deltas


def solution_part_one(s: str) -> int:
    levels = parse_input(s)
    safe_levels = [x for x in levels if _is_safe(x)]
    return len(safe_levels)


# Part two


def _dampen(xs: list[int]) -> Generator[None, None, list[int]]:
    yield xs
    for i in range(len(xs)):
        yield xs[:i] + xs[i + 1 :]


def solution_part_two(s: str) -> int:
    levels = parse_input(s)
    safe_levels = [level for level in levels if any([_is_safe(x) for x in _dampen(level)])]
    return len(safe_levels)


def main() -> None:
    s = problem_input()
    print(solution_part_one(s))
    print(solution_part_two(s))


if __name__ == "__main__":
    main()
