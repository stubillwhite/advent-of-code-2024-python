import functools
from collections import defaultdict
from importlib.resources import read_text
from typing import List, Mapping, Tuple

type Rules = Mapping[int, List[int]]

type Update = List[int]


def problem_input() -> str:
    return read_text("resources", "day-5-input.txt")


def _parse_input(s: str) -> Tuple[Rules, list[Update]]:
    (top, bottom) = s.split("\n\n")

    rules = defaultdict(list)
    for line in top.splitlines():
        page, dep = line.split("|")
        rules[int(page)].append(int(dep))

    updates = [[int(x) for x in line.split(",")] for line in bottom.splitlines()]

    return rules, updates


def _is_correctly_ordered(rules: Rules, update: Update) -> bool:
    satisfies_rules = [all([dep not in update[:idx] for dep in rules[page]]) for idx, page in enumerate(update)]
    return all(satisfies_rules)


def solution_part_one(s: str) -> int:
    rules, updates = _parse_input(s)
    correctly_ordered_updates = [u for u in updates if _is_correctly_ordered(rules, u)]
    return sum([update[(len(update) // 2)] for update in correctly_ordered_updates])


# Part two


def solution_part_two(s: str) -> int:
    rules, updates = _parse_input(s)

    def compare_deps(a: int, b: int) -> int:
        return -1 if b in rules[a] else 0

    incorrectly_ordered_updates = [u for u in updates if not _is_correctly_ordered(rules, u)]
    reordered_updates = [sorted(x, key=functools.cmp_to_key(compare_deps)) for x in incorrectly_ordered_updates]

    return sum([xs[len(xs) // 2] for xs in reordered_updates])


def main() -> None:
    s = problem_input()
    print(solution_part_one(s))
    print(solution_part_two(s))


if __name__ == "__main__":
    main()
