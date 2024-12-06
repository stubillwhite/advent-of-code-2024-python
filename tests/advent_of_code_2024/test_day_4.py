from advent_of_code_2024.day_4 import *


def example_input() -> str:
    return "\n".join(
        [
            "MMMSXXMASM",
            "MSAMXMSMSA",
            "AMXSXMAAMM",
            "MSAMASMSMX",
            "XMASAMXAMM",
            "XXAMMXXAMA",
            "SMSMSASXSS",
            "SAXAMASAAA",
            "MAMMMXMMMM",
            "MXMXAXMASX",
        ]
    )


def test_solution_part_one_given_example_input_then_example_result():
    assert solution_part_one(example_input()) == 18


def test_solution_part_one_given_problem_input_then_problem_result():
    assert solution_part_one(problem_input()) == 2560


def test_solution_part_two_given_example_input_then_example_result():
    assert solution_part_two(example_input()) == 9


def test_solution_part_two_given_problem_input_then_problem_result():
    assert solution_part_two(problem_input()) == 1910
