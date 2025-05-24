# lib/alphabet/rotation_table.py
from typing import Dict, List
from .alphabet import Alphabet
from transforms.sequence_ops import SequenceAdapter

MODES = {
    "normal": lambda x: x,
    "mirror": lambda x: list(reversed(x))
}

class RotationTable:
    """
    Constructs a table of rotated alphabets for use in polyalphabetic ciphers.

    Args:
        base: An Alphabet object.
        step: Rotation step.
        mode: Optional, "normal" or "mirror".

    Example:
        >>> from structures.alphabet import Alphabet
        >>> alpha = Alphabet.from_unicode_ranges("basic", [(65, 67)])
        >>> table = RotationTable(alpha, step=1)
        >>> table.lookup('A', 'B')
        'C'
    """

    def __init__(self, base: Alphabet, step: int, mode: str = "normal"):
        self.base = base
        self.step = step
        transform = MODES.get(mode, MODES["normal"])
        self.rows: Dict[int, List[str]] = {
            i: transform(row.data)
            for i, row in enumerate(SequenceAdapter.rotate_generator(base.sequence, step))
        }

    def __getitem__(self, index: int) -> List[str]:
        """
        Access a rotated alphabet row by index.

        >>> table[1]
        ['B', 'C', 'A']
        """
        return self.rows[index % len(self.rows)]

    def lookup(self, plain: str, key: str) -> str:
        """
        Look up encrypted character based on plaintext and key.

        Args:
            plain: Character to encrypt.
            key: Key character.

        Returns:
            Substituted character.

        Example:
            >>> table.lookup('A', 'B')
            'C'
        """
        row = self.base.sequence.index_of(key)
        col = self.base.sequence.index_of(plain)
        return self[row][col]

