# lib/sequences/transform.py
# lib/sequences/transform.py
# flytta till adapters/sequence_ops.py
# byta namn från sequence_ops.py -> sequence_adapter.py

from typing import Callable, Iterable, Iterator, List, TypeVar

from core.error import EmptySequenceError
from lib.math.rotation_math import normalize_shift, unique_rotation
from lib.sequences.registry import register
from transforms.list_ops import (
        yield_unique_rotation, 
        move_elements_to_front_variants,
)
from utils.validators import(
        ensure_not_empty,
        ensure_positive,
        ensure_not_equal
)



T = TypeVar("T")

__all__ = ["SequenceAdapter"]

class SequenceAdapter:
    """
    Stateless utility class for sequence transformations.

    Contains minimal core operations for manipulating symbol sequences.
    Used as building blocks in ciphers, alphabets, and matrix structures.
    """


    # --- Registered public transforms ---


    @staticmethod
    @register("identity")
    def identity(seq: List[T]) -> List[T]:
        """
        Return the sequence unchanged.

        Used as a no-op or neutral function in pipelines.
        """
        return seq


    @staticmethod
    @register("reverse")
    def reverse(seq: List[T]) -> List[T]:
        """
        Return the sequence in reversed order.

        Used to mirror a sequence, e.g. for reflexive transformations.
        """
        return list(reversed(seq))


    @staticmethod
    @register("sort")
    def sort(seq: List[T]) -> List[T]:
        """
        Return the sequence sorted by default Python order.

        Useful for normalizing symbol order before analysis or comparison.
        """
        return sorted(seq)


    # --- Core transformation tools ---


    @staticmethod
    def rotate(seq: List[T], shift: int) -> List[T]:
        """
        Rotate the sequence by the given shift (positive or negative).

        Used to create circular permutations of symbols.
        """
        ensure_not_empty(seq)
        normalized = normalize_shift(shift, len(seq))
        return seq[-normalized:] + seq[:-normalized] if normalized else list(seq)


    @staticmethod
    def rotate_generator(seq: List[T], step: int = 1) -> Iterator['Sequence[T]']:
        """
        Yield all unique cyclic rotations of the sequence using a step.

        Used to build rotation tables or to analyze cyclic structure.
        """
        from .sequence import Sequence
        ensure_non_empty(seq)
        ensure_not_equal(step, 0, "Step must be non-zero")
        
        # antingen (len(seq), step) eller (step, len(seq)) vilken är bäst?
        norm_step = normalize_shift(step, len(seq))
        expected = unique_rotation(norm_step, len(seq))
        
        for rotation in yield_unique_rotation(seq, norm_step, SequenceAdapter.rotate):
            yield Sequence(rotation)


    @staticmethod
    def move_elements_to_front(seq: List[T], elements: List[T]) -> Iterator[List[T]]:
        """
        Yield variants with selected elements moved to the front.

        Used for prioritization or reordering of symbol weight.
        """
        ensure_not_empty(seq)
        return move_elements_to_front_variants(seq, elements)


    @staticmethod
    def from_generator(n: int, generator_func: Callable[[int], List[T]], mode: str = 'default') -> List[List[T]]:
        """
        Generate multiple sequences using a given generator function.

        Used to construct multiple rotations, reflections, or pattern structures.
        """
        ensure_positive(n, "Must generate at least one sequence.")
        ensure_not_equal(n, 1, "Generating only one sequence is discouraged.")

        result = [generator_func(i) for i in range(n)]
        return [list(reversed(seq)) for seq in result] if mode == 'mirror' else result
