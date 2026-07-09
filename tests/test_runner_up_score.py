import pytest
from src.find_runnerup_score.util import find_runner_up_score


def test_runner_up_score_case1():
    scores = [2, 3, 6, 6, 5]
    assert find_runner_up_score(scores) == 5


def test_runner_up_score_case2():
    scores = [1, 2, 3, 4, 5]
    assert find_runner_up_score(scores) == 4


def test_runner_up_score_with_duplicates():
    scores = [10, 10, 9, 8, 8]
    assert find_runner_up_score(scores) == 9


def test_runner_up_score_negative_numbers():
    scores = [-1, -2, -3, -4]
    assert find_runner_up_score(scores) == -2


def test_runner_up_score_unsorted_list():
    scores = [7, 3, 9, 5, 9, 7]
    assert find_runner_up_score(scores) == 7


def test_runner_up_score_two_unique_values():
    scores = [100, 50, 100]
    assert find_runner_up_score(scores) == 50


def test_runner_up_score_all_same():
    scores = [5, 5, 5, 5]

    with pytest.raises(ValueError):
        find_runner_up_score(scores)