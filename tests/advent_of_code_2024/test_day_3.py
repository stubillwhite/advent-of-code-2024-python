from advent_of_code_2024.day_3 import *


def example_input_one() -> str:
    return "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"


def example_input_two() -> str:
    return "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"


def test_solution_part_one_given_example_input_then_example_result():
    assert solution_part_one(example_input_one()) == 161


def test_solution_part_one_given_problem_input_then_problem_result():
    assert solution_part_one(problem_input()) == 184122457


def test_solution_part_two_given_example_input_then_example_result():
    assert solution_part_two(example_input_two()) == 48


def test_solution_part_two_given_problem_input_then_problem_result():
    assert solution_part_two(problem_input()) == 107862689
