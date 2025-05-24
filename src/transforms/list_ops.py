# src/transforms/list_ops.py

from typing import Callable, Iterator, TypeVar, List

T = TypeVar("T")


def yield_unique_rotations(data: List[T], step: int, rot_func: Callable[[List[T], int], List[T]]) -> Iterator[List[T]]:
    """
    Yields unique rotations of `data` using a step and a rotation function.

    Args:
        data: The list to rotate.
        step: The amount to increment each rotation.
        rot_func: A function that takes (list, current_index) and returns a rotated list.

    Returns:
        Iterator of unique rotations.

    Example:
        >>> from transforms.list_ops import yield_unique_rotations
        >>> list(yield_unique_rotations(['A', 'B', 'C'], 1, lambda d, i: d[-i % 3:] + d[:-i % 3]))
        [['A', 'B', 'C'], ['C', 'A', 'B'], ['B', 'C', 'A']]
    """
    seen = set()
    current = 0
    while current not in seen:
        seen.add(current)
        yield rot_func(data, current)
        current = (current + step) % len(data)


def move_elements_to_front_variants(seq: List[T], elements: List[T]) -> Iterator[List[T]]:
    """
    Generate sequence variants with specified elements moved to the front.

    Args:
        seq: Original list.
        elements: Elements to move.

    Yields:
        Variants with one element moved to front per variant.

    Example:
        >>> list(move_elements_to_front_variants(['A', 'B', 'C'], ['C']))
        [['C', 'A', 'B']]
    """
    for element in elements:
        if element in seq:
            temp = list(seq)
            temp.remove(element)
            yield [element] + temp

