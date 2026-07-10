from src.word_order.util import get_word_order


def test_sample_case():
    words = [
        "bcdef",
        "abcdefg",
        "bcde",
        "bcdef"
    ]

    assert get_word_order(words) == (3, [2, 1, 1])


def test_all_unique():
    words = ["a", "b", "c", "d"]

    assert get_word_order(words) == (4, [1, 1, 1, 1])


def test_all_same():
    words = ["hello", "hello", "hello"]

    assert get_word_order(words) == (1, [3])


def test_empty_list():
    assert get_word_order([]) == (0, [])


def test_mixed_words():
    words = [
        "apple",
        "banana",
        "apple",
        "orange",
        "banana",
        "apple"
    ]

    assert get_word_order(words) == (3, [3, 2, 1])


def test_single_word():
    words = ["python"]

    assert get_word_order(words) == (1, [1])


def test_case_sensitive():
    words = ["Python", "python", "Python"]

    assert get_word_order(words) == (2, [2, 1])