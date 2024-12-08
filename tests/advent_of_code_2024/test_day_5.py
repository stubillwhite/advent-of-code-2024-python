from advent_of_code_2024.day_5 import *


def example_input() -> str:
    return "\n".join(
        [
            "47|53",
            "97|13",
            "97|61",
            "97|47",
            "75|29",
            "61|13",
            "75|53",
            "29|13",
            "97|29",
            "53|29",
            "61|53",
            "97|53",
            "61|29",
            "47|13",
            "75|47",
            "97|75",
            "47|61",
            "75|61",
            "47|29",
            "75|13",
            "53|13",
            "",
            "75,47,61,53,29",
            "97,61,53,29,13",
            "75,29,13",
            "75,97,47,61,53",
            "61,13,29",
            "97,13,75,29,47",
        ]
    )


def test_solution_part_one_given_example_input_then_example_result():
    assert solution_part_one(example_input()) == 143


def test_solution_part_one_given_problem_input_then_problem_result():
    assert solution_part_one(problem_input()) == 5747


def test_solution_part_two_given_example_input_then_example_result():
    assert solution_part_two(example_input()) == 123


def test_solution_part_two_given_problem_input_then_problem_result():
    assert solution_part_two(problem_input()) == 5502
