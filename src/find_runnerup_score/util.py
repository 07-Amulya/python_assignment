def find_runner_up_score(scores):
    """
    Returns the runner-up (second highest unique) score.

    Args:
        scores (list): List of integer scores.

    Returns:
        int: Runner-up score.

    Raises:
        ValueError: If there are fewer than two unique scores.
    """

    unique_scores = sorted(set(scores), reverse=True)

    if len(unique_scores) < 2:
        raise ValueError("At least two unique scores are required.")

    return unique_scores[1]