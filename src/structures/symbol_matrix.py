from typing import List, Dict
from dataclasses import dataclass, field


@dataclass(frozen=True)
class RotationMatrix:
    """
    A 2D rotation matrix for substitution ciphers.

    Each row represents a rotated version of a base alphabet.
    The matrix supports lookup by both index and character,
    as well as vector extraction and integer conversion for analysis.

    Attributes:
        base_sequence: The original sequence used as the base for rotations.
        matrix: A list of rows, each a rotated version of the base sequence.

    Example:
        >>> base = ['A', 'B', 'C']
        >>> rotations = [['A', 'B', 'C'], ['B', 'C', 'A'], ['C', 'A', 'B']]
        >>> rm = RotationMatrix(base_sequence=base, matrix=rotations)
        >>> rm.lookup(1, 2)
        'A'
        >>> rm.lookup_char('A', 'B')
        'B'
        >>> rm.get_row_vector(2)
        ['C', 'A', 'B']
        >>> rm.get_column_vector(1)
        ['B', 'C', 'A']
        >>> rm.as_int_matrix()
        [[0, 1, 2], [1, 2, 0], [2, 0, 1]]
    """

    base_sequence: List[str]
    matrix: List[List[str]]
    index_map: Dict[str, int] = field(init=False)

    def __post_init__(self):
        """Initializes the index mapping from characters to indices."""
        object.__setattr__(self, 'index_map', {char: idx for idx, char in enumerate(self.base_sequence)})

    def lookup(self, row: int, col: int) -> str:
        """Returns the character at a specific row and column index."""
        return self.matrix[row % len(self.matrix)][col % len(self.base_sequence)]

    def lookup_char(self, plain: str, key: str) -> str:
        """Returns the cipher character based on plaintext and key character."""
        row = self.index_map.get(key)
        col = self.index_map.get(plain)
        if row is None or col is None:
            return '?'
        return self.lookup(row, col)

    def get_row_vector(self, index: int) -> List[str]:
        """Retrieves a row from the matrix corresponding to a rotation."""
        return self.matrix[index % len(self.matrix)]

    def get_column_vector(self, index: int) -> List[str]:
        """Retrieves a column from the matrix based on base sequence index."""
        return [row[index % len(self.base_sequence)] for row in self.matrix]

    def as_int_matrix(self) -> List[List[int]]:
        """Returns the matrix as integer indices according to base_sequence."""
        return [[self.index_map.get(char, -1) for char in row] for row in self.matrix]

