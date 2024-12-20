from importlib.resources import files
from typing import Callable, List, Tuple


def parse_input(s: str) -> List[Tuple[int, List[int]]]:

    def parse_line(line: str) -> Tuple[int, List[int]]:
        result, operands = line.split(":")
        return int(result), list(map(int, operands.split()))

    return [parse_line(line) for line in s.splitlines()]


BinaryOperator = Callable[[int, int], int]


def mult(a: int, b: int) -> int:
    return a * b


def add(a: int, b: int) -> int:
    return a + b


def concat(a: int, b: int) -> int:
    return int(str(a) + str(b))


def satisfiable(operators: List[BinaryOperator], result: int, operands: List[int]) -> bool:
    if len(operands) == 1:
        return operands[0] == result
    else:
        return any(satisfiable(operators, result, [op(operands[0], operands[1])] + operands[2:]) for op in operators)


def problem_input() -> str:
    return files("resources").joinpath("day-7-input.txt").read_text()


def solution_part_one(s: str) -> int:
    sums = parse_input(s)
    operators = [add, mult]
    valid = [s for s in sums if satisfiable(operators, s[0], s[1])]
    return sum([result for result, _ in valid])


# Part two


def solution_part_two(s: str) -> int:
    sums = parse_input(s)
    operators = [add, mult, concat]
    valid = [s for s in sums if satisfiable(operators, s[0], s[1])]
    return sum([result for result, _ in valid])


def main() -> None:
    s = problem_input()
    print(solution_part_one(s))
    print(solution_part_two(s))


if __name__ == "__main__":
    main()
