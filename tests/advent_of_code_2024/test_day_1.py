from advent_of_code_2024.day_1 import *


def example_input() -> str:
    return "\n".join(
        [
            "3   4",
            "4   3",
            "2   5",
            "1   3",
            "3   9",
            "3   3",
        ]
    )


def test_solution_part_one_given_example_input_then_example_result():
    assert solution_part_one(example_input()) == 11


def test_solution_part_one_given_problem_input_then_problem_result():
    assert solution_part_one(problem_input()) == 2378066


def test_solution_part_two_given_example_input_then_example_result():
    assert solution_part_two(example_input()) == 31


def test_solution_part_two_given_problem_input_then_problem_result():
    assert solution_part_two(problem_input()) == 18934359
