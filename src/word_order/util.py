from collections import Counter


def get_word_order(words):
    """
    Returns the count of distinct words and their frequencies.

    Args:
        words (list): List of words.

    Returns:
        tuple: (number_of_distinct_words, frequency_list)
    """

    counts = Counter(words)

    return len(counts), list(counts.values())