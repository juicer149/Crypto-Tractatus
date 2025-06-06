# src/transforms/list_ops.py

from typing import Callable, Iterator, TypeVar, List

# kanske byta namn till rotation_math?
from math.sequence_math import normalize_shift 

from utils.validators import (
        ensure_not_empty,
        ensure_not_equal,
        ensure_greater_then,
)


T = TypeVar("T")


def rotate(seq: List[T], shift: int) -> List[T]:
    """
    Rotate the sequence by a given shift (positive or negative).
    """
    ensure_not_empty(seq)
    normalized = normalize_shift(shift, len(seq))
    return seq[-normalized:] + seq[:-normalized] if normalized else list(seq)


def rotate_generator(seq: List[T], step: int = 1) -> Iterator[List[T]]:
    """
    Yield all unique cyclic rotations of a sequence using a step.
    """
    ensure_not_empty(seq)
    ensure_not_equal(step, 0, "Step must be non-zero")

    norm_step = normalize_shift(step, len(seq))
    seen = set()
    current = 0
    while current not in seen:
        seen.add(current)
        yield rotate(seq, current)
        current = (current + norm_step) % len(seq)


def yield_unique_rotation(
    seq: List[T],
    step: int,
    rot_func: Callable[[List[T], int], List[T]]
) -> Iterator[List[T]]:
    """
    Core generator used for rotating a sequence with uniqueness guarantee.
    """
    ensure_not_empty(seq)
    ensure_not_equal(step, 0)
    seen = set()
    current = 0
    while current not in seen:
        seen.add(current)
        yield rot_func(seq, current)
        current = (current + step) % len(seq)


def move_elements_to_index(seq: List[T], elements: List[T], index: int = 0) -> Iterator[List[T]]:
    """
    Generate sequence variants with specified elements moved to index, standard 0.

    Args:
        seq: Original list.
        elements: Elements to move.
        index: index to move element to.

    Yields:
        Variants with one element moved to index per variant.

    Example:
        >>> list(move_elements_to_index(['A', 'B', 'C'], ['C']))
        [['C', 'A', 'B']]

    """
    for element in elements:
        if element in seq:
            temp = list(seq)
            temp.remove(element)
            temp.insert(index, element)
            yield [element] + temp


def generate_sequence_lists(n: int, generator_func: Callable[[int], List[T]]) -> List[List[T]]:
    """
    Generate multiple raw lists from a generator function.

    Args:
        n: Number of sequences to generate (must be > 1).
        generator_func: A function taking an index and returning a list.

    Returns:
        A list of lists generated by the function.

    Example:
        >>> def gen(i): return [chr(65 + (i + j) % 3) for j in range(3)]
        >>> generate_sequence_lists(3, gen)
        [['A', 'B', 'C'], ['B', 'C', 'A'], ['C', 'A', 'B']]
    """
    ensure_greater_then(n, 1, "Must generate more than one sequence.")
    return [generator_func(i) for i in range(n)]


def rotate_sequence_by_lookup_values(
    keys: List[str],
    reference: List[str]
) -> List[List[str]]:
    """
    For each key, rotate the reference list so that the key is at index 0.

    This is used in ciphers like Vigenère to generate rotation rows based on a key sequence.

    Args:
        keys: Elements that determine how the reference is rotated.
        reference: The list to rotate from (e.g., an alphabet).

    Returns:
        A list of rotated lists based on key positions in the reference.

    Example:
        >>> rotate_sequence_by_lookup_values(["B", "A"], ["A", "B", "C"])
        [['B', 'C', 'A'], ['A', 'B', 'C']]
    """
    seen = {}
    result = []
    for key in keys:
        if key not in seen:
            idx = reference.index(key)
            seen[key] = reference[idx:] + reference[:idx]
        result.append(seen[key])
    return result


def unique_preserve_order(seq: List[str]) -> List[str]:
    """
    Return a list with duplicates removed, preserving the original order.

    Useful for reducing keywords before generating cipher mappings.
    
    Example:
        >>> unique_preserve_order(["L", "E", "M", "O", "N", "L"])
        ['L', 'E', 'M', 'O', 'N']
    """
    seen = set()
    result = []
    for item in seq:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

