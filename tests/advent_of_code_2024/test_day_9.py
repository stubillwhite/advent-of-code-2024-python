import unittest

from advent_of_code_2024.day_9 import *


def example_input() -> str:
    return "2333133121414131402"


def test_solution_part_one_given_example_input_then_example_result():
    assert solution_part_one(example_input()) == 1928


def test_solution_part_one_given_problem_input_then_problem_result():
    assert solution_part_one(problem_input()) == 6200294120911


def test_solution_part_two_given_example_input_then_example_result():
    assert solution_part_two(example_input()) == 2858


def test_solution_part_two_given_problem_input_then_problem_result():
    assert solution_part_two(problem_input()) == 6227018762750
