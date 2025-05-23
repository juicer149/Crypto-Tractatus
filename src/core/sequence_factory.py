# lib/sequences/factory.py
from typing import Callable, List, TypeVar
from .sequence import Sequence

T = TypeVar("T")

class SequenceFactory:
    """
    Factory class for creating sequences from generators.

    Provides a method to construct multiple Sequence[T] instances from a generator function.
    """

    @staticmethod
    def from_generator(n: int, generator_func: Callable[[int], List[T]]) -> List[Sequence[T]]:
        """
        Generate `n` sequences using a generator function.

        Args:
            n: Number of sequences to generate.
            generator_func: Function that takes an index and returns a list of elements.

        Returns:
            List of Sequence[T] objects.

        Raises:
            ValueError: If n <= 1.

        Example:
            >>> def f(i): return [chr(65 + (i + j) % 3) for j in range(3)]
            >>> sequences = SequenceFactory.from_generator(3, f)
            >>> [s.data for s in sequences]
            [['A', 'B', 'C'], ['B', 'C', 'A'], ['C', 'A', 'B']]
        """

        if n <= 1:
            raise ValueError("Need at least 2 sequences.")
        return [Sequence(generator_func(i)) for i in range(n)]



