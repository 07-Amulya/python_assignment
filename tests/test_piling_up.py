from src.piling_up.util import can_pile_up


def test_sample_yes():
    assert can_pile_up([4, 3, 2, 1, 3, 4]) == "Yes"


def test_sample_no():
    assert can_pile_up([1, 3, 2]) == "No"


def test_single_block():
    assert can_pile_up([5]) == "Yes"


def test_already_descending():
    assert can_pile_up([5, 4, 3, 2, 1]) == "Yes"


def test_already_ascending():
    assert can_pile_up([1, 2, 3, 4, 5]) == "Yes"


def test_equal_blocks():
    assert can_pile_up([2, 2, 2, 2]) == "Yes"


def test_complex_yes():
    assert can_pile_up([10, 9, 8, 7, 6, 5]) == "Yes"


def test_complex_no():
    assert can_pile_up([2, 1, 5, 4, 3]) == "No"


def test_empty_list():
    assert can_pile_up([]) == "Yes"