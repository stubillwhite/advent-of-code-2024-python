from importlib.resources import files
from itertools import combinations, groupby
from typing import Callable, Dict, Iterable, List, Tuple

Location = Tuple[int, int]

Grid = Dict[Location, str]


def problem_input() -> str:
    return files("resources").joinpath("day-8-input.txt").read_text()


def solution_part_one(s: str) -> int:
    grid = _parse_input(s)
    antinodes = _detect_antinodes_in_grid(grid, _immediate_antinode_detector)
    return len(set(antinodes))


# Part two


def solution_part_two(s: str) -> int:
    grid = _parse_input(s)
    antinodes = _detect_antinodes_in_grid(grid, _harmonic_antinode_detector)
    return len(set(antinodes))


def main() -> None:
    s = problem_input()
    print(solution_part_one(s))
    print(solution_part_two(s))


def _parse_input(s: str) -> Grid:
    return {(x, y): ch for (y, line) in enumerate(s.splitlines()) for (x, ch) in enumerate(line)}


def _invert_mapping[A, B](d: Dict[A, B]) -> Dict[B, List[A]]:
    vals_to_keys = [(v, k) for k, v in d.items()]
    return {v: list([k for _, k in ks]) for v, ks in groupby(sorted(vals_to_keys), key=lambda vk: vk[0])}


AntinodeDetector = Callable[[Grid, Location, Location], List[Location]]


def _detect_antinodes_in_grid(grid: Grid, antinode_detector: AntinodeDetector) -> List[Location]:
    antenna_locations = _invert_mapping(grid)

    return [
        loc
        for antenna_id in antenna_locations.keys()
        for l1, l2 in combinations(antenna_locations[antenna_id], 2)
        for loc in antinode_detector(grid, l1, l2)
        if antenna_id != "."
    ]


def _immediate_antinode_detector(grid: Grid, l1: Location, l2: Location) -> List[Location]:
    x1, y1 = l1
    x2, y2 = l2

    return [loc for loc in [(x2 + (x2 - x1), y2 + (y2 - y1)), (x1 + (x1 - x2), y1 + (y1 - y2))] if loc in grid.keys()]


def _harmonic_antinode_detector(grid: Grid, l1: Location, l2: Location) -> List[Location]:
    def harmonics(a: Location, b: Location) -> Iterable[Location]:
        x, y = a[0], a[1]
        dx, dy = a[0] - b[0], a[1] - b[1]
        while (x, y) in grid.keys():
            yield x, y
            x, y = x + dx, y + dy

    return list(harmonics(l1, l2)) + list(harmonics(l2, l1))


if __name__ == "__main__":
    main()
