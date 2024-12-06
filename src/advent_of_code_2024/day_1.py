from importlib.resources import files
from itertools import groupby


def problem_input() -> str:
    return files("resources").joinpath("day-1-input.txt").read_text()


def _parse_input(s: str) -> list[list[int]]:
    def transpose[A](rows: list[list[A]]) -> list[list[A]]:
        return [list(col) for col in zip(*rows)]

    words = [[int(x) for x in line.split()] for line in s.splitlines()]
    return transpose(words)


def solution_part_one(s: str) -> int:
    (l1, l2) = [sorted(x) for x in _parse_input(s)]
    distances = [abs(xs[0] - xs[1]) for xs in zip(l1, l2)]
    return sum(distances)


# Part two


def solution_part_two(s: str) -> int:
    (l1, l2) = _parse_input(s)
    frequencies = {k: len(list(vs)) for k, vs in groupby(sorted(l2))}
    similarities = [x * frequencies.get(x, 0) for x in l1]
    return sum(similarities)


def main() -> None:
    s = problem_input()
    print(solution_part_one(s))
    print(solution_part_two(s))


if __name__ == "__main__":
    main()
