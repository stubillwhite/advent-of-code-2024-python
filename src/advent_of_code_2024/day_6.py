from copy import deepcopy
from dataclasses import dataclass
from enum import Enum, auto
from importlib.resources import files
from typing import Dict, List, Set, Tuple


def problem_input() -> str:
    return files("resources").joinpath("day-6-input.txt").read_text()


class Facings:
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4


Facing = int
Location = Tuple[int, int]
Grid = Dict[Location, str]


class GuardStatus(Enum):
    MOVING = auto()
    LEFT_AREA = auto()
    LOOPING = auto()


@dataclass
class State:
    grid: Grid
    facing: Facing
    location: Location
    visited: Set[Tuple[Facing, Location]]
    guard_status: GuardStatus


def _parse_input(s: str) -> State:
    grid = {(x, y): ch for (y, line) in enumerate(s.splitlines()) for (x, ch) in enumerate(line)}
    facing = Facings.NORTH
    location = [loc for loc, s in grid.items() if s == "^"][0]
    visited = {(facing, location)}
    guard_status = GuardStatus.MOVING

    grid[location] = "."

    return State(grid, facing, location, visited, guard_status)


def _turn_right(facing: Facing) -> Facing:
    return (facing % 4) + 1


def _location_ahead(location: Location, facing: Facing) -> Location:
    deltas = {Facings.NORTH: (0, -1), Facings.EAST: (1, 0), Facings.SOUTH: (0, 1), Facings.WEST: (-1, 0)}

    x, y = location
    dx, dy = deltas[facing]
    return x + dx, y + dy


def _next_state(state: State) -> None:
    new_location = _location_ahead(state.location, state.facing)

    if (state.facing, new_location) in state.visited:
        state.guard_status = GuardStatus.LOOPING

    elif state.grid.get(new_location, None) == "#":
        state.facing = _turn_right(state.facing)

    elif new_location in state.grid:
        state.visited.add((state.facing, new_location))
        state.location = new_location

    else:
        state.guard_status = GuardStatus.LEFT_AREA


def _execute_until_complete(state: State) -> None:
    while state.guard_status not in (GuardStatus.LEFT_AREA, GuardStatus.LOOPING):
        _next_state(state)


def _find_locations_visited(s: str) -> Set[Location]:
    state = _parse_input(s)
    _execute_until_complete(state)
    return set([location for facing, location in state.visited])


def solution_part_one(s: str) -> int:
    locations_visited = _find_locations_visited(s)
    return len(locations_visited)


# Part two


def solution_part_two(s: str) -> int:
    locations_visited = _find_locations_visited(s)
    obstacle_locations = _find_potential_obstacle_locations(locations_visited, s)
    return len(obstacle_locations)


def _find_potential_obstacle_locations(locations_visited: Set[Location], s: str) -> List[Location]:
    initial_state = _parse_input(s)
    state = deepcopy(initial_state)

    obstacle_locations = []
    for location_on_path in locations_visited:
        state.grid[location_on_path] = "#"
        _execute_until_complete(state)

        if state.guard_status == GuardStatus.LOOPING:
            obstacle_locations += [location_on_path]

        state.facing = initial_state.facing
        state.location = initial_state.location
        state.visited = {(state.facing, state.location)}
        state.guard_status = GuardStatus.MOVING
        state.grid[location_on_path] = "."

    return obstacle_locations


def main() -> None:
    s = problem_input()
    print(solution_part_one(s))
    print(solution_part_two(s))


if __name__ == "__main__":
    main()
