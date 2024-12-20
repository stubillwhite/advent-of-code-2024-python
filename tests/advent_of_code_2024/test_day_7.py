from advent_of_code_2024.day_7 import *


def example_input() -> str:
    return "\n".join(
        [
            "190: 10 19",
            "3267: 81 40 27",
            "83: 17 5",
            "156: 15 6",
            "7290: 6 8 6 15",
            "161011: 16 10 13",
            "192: 17 8 14",
            "21037: 9 7 18 13",
            "292: 11 6 16 20",
        ]
    )


def test_solution_part_one_given_example_input_then_example_result():
    assert solution_part_one(example_input()) == 3749


def test_solution_part_one_given_problem_input_then_problem_result():
    assert solution_part_one(problem_input()) == 932137732557


def test_solution_part_two_given_example_input_then_example_result():
    assert solution_part_two(example_input()) == 11387


def test_solution_part_two_given_problem_input_then_problem_result():
    assert solution_part_two(problem_input()) == 661823605105500
