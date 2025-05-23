# lib/sequences/transform.py
# lib/sequences/transform.py

from typing import Callable, Iterable, Iterator, List, TypeVar
from lib.math.rotation_math import normalize_shift, unique_rotation
from lib.sequences.registry import register
import warnings

T = TypeVar("T")

__all__ = ["SequenceTransform"]

class SequenceTransform:
    """
    Stateless utility class for sequence transformations.

    Provides both a set of named, registry-based transformations
    (used via configuration or plug-in architecture), as well as core
    utilities for rotation and sequence reordering.

    This class is central to the manipulation of Alphabet, Sequence,
    and RotationTable components.
    """

    # --- Registered public transforms ---

    @staticmethod
    @register("identity")
    def identity(seq: List[T]) -> List[T]:
        """
        Return the sequence unchanged.

        >>> SequenceTransform.identity(['A', 'B', 'C'])
        ['A', 'B', 'C']
        """
        return seq

    @staticmethod
    @register("reverse")
    def reverse(seq: List[T]) -> List[T]:
        """
        Return a reversed version of the sequence.

        >>> SequenceTransform.reverse(['A', 'B', 'C'])
        ['C', 'B', 'A']
        """
        return list(reversed(seq))

    @staticmethod
    @register("sort")
    def sort(seq: List[T]) -> List[T]:
        """
        Return the sequence sorted (default Python order).

        >>> SequenceTransform.sort(['B', 'C', 'A'])
        ['A', 'B', 'C']
        """
        return sorted(seq)

    # --- Core transformation tools ---

    @staticmethod
    def rotate(seq: List[T], shift: int) -> List[T]:
        """
        Rotate a sequence by a given shift.

        >>> SequenceTransform.rotate(['A', 'B', 'C'], 1)
        ['C', 'A', 'B']
        >>> SequenceTransform.rotate(['A', 'B', 'C'], -1)
        ['B', 'C', 'A']
        """
        if not seq:
            raise ValueError("Cannot rotate an empty sequence.")
        length = len(seq)
        normalized = normalize_shift(shift, length)
        return seq[-normalized:] + seq[:-normalized] if normalized else list(seq)

    @staticmethod
    def rotate_generator(seq: List[T], step: int = 1) -> Iterator['Sequence[T]']:
        """
        Generate all distinct rotations of a sequence by a given step.

        >>> gen = SequenceTransform.rotate_generator(['A', 'B', 'C'], 1)
        >>> [next(gen).data for _ in range(3)]
        [['A', 'B', 'C'], ['C', 'A', 'B'], ['B', 'C', 'A']]
        """
        from .sequence import Sequence
        if not seq:
            raise ValueError("Cannot rotate an empty sequence.")
        if step == 0:
            raise ValueError("Step must be non-zero.")
        length = len(seq)
        norm_step = normalize_shift(step, length)
        expected = unique_rotation(length, norm_step)

        seen = set()
        current = 0
        while current not in seen:
            seen.add(current)
            yield Sequence(SequenceTransform.rotate(seq, current))
            current = (current + norm_step) % length

        if len(seen) != expected:
            warnings.warn("Generated fewer unique rotations than expected.")

    @staticmethod
    def move_elements_to_front(seq: List[T], elements: List[T]) -> Iterator[List[T]]:
        """
        Yield versions of the sequence with specified elements moved to front.

        >>> list(SequenceTransform.move_elements_to_front(['A', 'B', 'C'], ['C']))
        [['C', 'A', 'B']]
        """
        if not seq:
            raise ValueError("Cannot manipulate an empty sequence.")
        for element in elements:
            if element in seq:
                temp = list(seq)
                temp.remove(element)
                yield [element] + temp

    @staticmethod
    def from_generator(n: int, generator_func: Callable[[int], List[T]], mode: str = 'default') -> List[List[T]]:
        """
        Generate n sequences using a custom generator function.

        >>> def gen(i): return [chr(65 + (j + i) % 3) for j in range(3)]
        >>> SequenceTransform.from_generator(3, gen)
        [['A', 'B', 'C'], ['B', 'C', 'A'], ['C', 'A', 'B']]
        """
        if n <= 0:
            raise ValueError("Cannot generate zero or negative number of sequences.")
        if n == 1:
            raise ValueError("Generating only one sequence is discouraged.")

        result = [generator_func(i) for i in range(n)]
        if mode == 'mirror':
            return [list(reversed(seq)) for seq in result]
        return result

