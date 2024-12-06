import re
from dataclasses import dataclass, replace
from functools import reduce
from importlib.resources import files
from typing import Any


def problem_input() -> str:
    return files("resources").joinpath("day-3-input.txt").read_text()


@dataclass
class Instruction:
    opcode: str
    args: list[Any]


@dataclass
class State:
    total: int = 0
    can_disable: bool = True
    is_disabled: bool = False


def _parse_input(s: str) -> list[Instruction]:
    regex = r"(mul\(\d+,\d+\))|(do\(\)|(don't\(\)))"

    def parse_instr(instr: str) -> Instruction:
        opcode, args = re.match(r"(.+)\((.*)\)", instr).groups()
        match opcode:
            case "mul":
                return Instruction(opcode, [int(x) for x in args.split(",")])
            case "do" | "don't":
                return Instruction(opcode, [])

    return [parse_instr(m.group(0)) for m in re.finditer(regex, s)]


def execute_instruction(state: State, instr: Instruction) -> State:
    match instr:
        case Instruction("mul", args):
            return state if state.is_disabled else replace(state, total=state.total + args[0] * args[1])

        case Instruction("do", args):
            return replace(state, is_disabled=False)

        case Instruction("don't", args):
            return replace(state, is_disabled=state.can_disable)


def solution_part_one(s: str) -> int:
    instructions = _parse_input(s)
    state = State(can_disable=False)
    return reduce(execute_instruction, instructions, state).total


# Part two


def solution_part_two(s: str) -> int:
    instructions = _parse_input(s)
    state = State()
    return reduce(execute_instruction, instructions, state).total


def main() -> None:
    s = problem_input()
    print(solution_part_one(s))
    print(solution_part_two(s))


if __name__ == "__main__":
    main()
