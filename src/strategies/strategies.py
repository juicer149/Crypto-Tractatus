from typing import Callable


def round_robin_strategy(pos: int, total: int) -> int:
    """
    Selects index in round-robin fashion.

    >>> [round_robin_strategy(i, 3) for i in range(6)]
    [0, 1, 2, 0, 1, 2]
    """
    return pos % total


def pattern_strategy(pos: int, pattern: list[int]) -> int:
    """
    Selects index from a custom pattern list.

    >>> pattern_strategy(2, [0, 3, 1, 4, 2])
    1
    """
    return pattern[pos % len(pattern)]


def static_strategy(_: int, index: int) -> int:
    """
    Always returns the same index, used for static ciphers.

    >>> [static_strategy(i, 2) for i in range(4)]
    [2, 2, 2, 2]
    """
    return index

