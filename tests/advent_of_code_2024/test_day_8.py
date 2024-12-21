import unittest

from advent_of_code_2024.day_8 import *


def example_input() -> str:
    return "\n".join(
        [
            "............",
            "........0...",
            ".....0......",
            ".......0....",
            "....0.......",
            "......A.....",
            "............",
            "............",
            "........A...",
            ".........A..",
            "............",
            "............",
        ]
    )


def test_solution_part_one_given_example_input_then_example_result():
    assert solution_part_one(example_input()) == 14


def test_solution_part_one_given_problem_input_then_problem_result():
    assert solution_part_one(problem_input()) == 256


def test_solution_part_two_given_example_input_then_example_result():
    assert solution_part_two(example_input()) == 34


def test_solution_part_two_given_problem_input_then_problem_result():
    assert solution_part_two(problem_input()) == 1005
