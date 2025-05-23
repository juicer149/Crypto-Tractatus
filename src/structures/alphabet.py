# lib/alphabet/alphabet.py
from typing import List, Tuple
from dataclasses import dataclass
from structures.sequence import Sequence

@dataclass(frozen=True)
class Alphabet:
    """
    Represents an immutable character set used in ciphers.

    Attributes:
        name (str): The name of the alphabet.
        sequence (Sequence[str]): Ordered, unique characters used for substitution.

    Example:
        >>> Alphabet.from_unicode_ranges("basic", [(65, 67)])
        Alphabet(name='basic', sequence=Sequence(data=['A', 'B', 'C']))
    """

    name: str
    sequence: Sequence[str]

    @classmethod
    def from_unicode_ranges(cls, name: str, ranges: List[Tuple[int, int]], extras: List[int] = []) -> 'Alphabet':
        """
        Create an Alphabet from Unicode ranges and optional extra characters.

        Args:
            name: A label for the alphabet.
            ranges: List of (start, end) tuples for Unicode ranges.
            extras: Optional list of Unicode code points to include.

        Returns:
            Alphabet instance with unique characters.

        Raises:
            ValueError: If characters are not unique.

        Example:
            >>> Alphabet.from_unicode_ranges("example", [(65, 66)], [67])
            Alphabet(name='example', sequence=Sequence(data=['A', 'B', 'C']))
        """
        chars = [chr(c) for start, end in ranges for c in range(start, end+1)] + [chr(c) for c in extras]
        seq = Sequence(chars)
        seq.validate_unique()
        return cls(name, seq)

