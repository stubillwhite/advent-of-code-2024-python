from advent_of_code_2024.day_2 import *


def example_input() -> str:
    return "\n".join(
        [
            "7 6 4 2 1",
            "1 2 7 8 9",
            "9 7 6 2 1",
            "1 3 2 4 5",
            "8 6 4 4 1",
            "1 3 6 7 9",
        ]
    )


def test_solution_part_one_given_example_input_then_example_result():
    assert solution_part_one(example_input()) == 2


def test_solution_part_one_given_problem_input_then_problem_result():
    assert solution_part_one(problem_input()) == 306


def test_solution_part_two_given_example_input_then_example_result():
    assert solution_part_two(example_input()) == 4


def test_solution_part_two_given_problem_input_then_problem_result():
    assert solution_part_two(problem_input()) == 366
