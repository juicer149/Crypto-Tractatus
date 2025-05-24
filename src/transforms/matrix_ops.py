from typing import List
from lib.structures.rotation_matrix import RotationMatrix
from adapters.sequence_adapter import SequenceAdapter

class MatrixTransform:
    """
    A utility class for transforming RotationMatrix instances.

    Supports operations like row/column reordering, mirroring, and transposition
    which can be used for reflexive cipher design and structure mutation.
    """

    @staticmethod
    def rotate_rows(matrix: RotationMatrix, shift: int) -> RotationMatrix:
        """
        Rotates each row's content by `shift` (NOT row positions).

        >>> base = ['A', 'B', 'C']
        >>> mat = [['A', 'B', 'C'], ['B', 'C', 'A'], ['C', 'A', 'B']]
        >>> rm = RotationMatrix(base_sequence=base, matrix=mat)
        >>> mt = MatrixTransform.rotate_rows(rm, 1)
        >>> mt.matrix[0]
        ['C', 'A', 'B']
        """
        new_matrix = [SequenceAdapter.rotate(row, shift) for row in matrix.matrix]
        return RotationMatrix(base_sequence=matrix.base_sequence, matrix=new_matrix)

    @staticmethod
    def mirror_rows(matrix: RotationMatrix) -> RotationMatrix:
        """
        Reverses all rows in the matrix.

        >>> base = ['A', 'B', 'C']
        >>> mat = [['A', 'B', 'C'], ['B', 'C', 'A']]
        >>> rm = RotationMatrix(base_sequence=base, matrix=mat)
        >>> mt = MatrixTransform.mirror_rows(rm)
        >>> mt.matrix[0]
        ['C', 'B', 'A']
        """
        new_matrix = [list(reversed(row)) for row in matrix.matrix]
        return RotationMatrix(base_sequence=matrix.base_sequence, matrix=new_matrix)

    @staticmethod
    def transpose(matrix: RotationMatrix) -> RotationMatrix:
        """
        Transposes the matrix (rows become columns and vice versa).

        >>> base = ['A', 'B', 'C']
        >>> mat = [['A', 'B', 'C'], ['D', 'E', 'F']]
        >>> rm = RotationMatrix(base_sequence=base, matrix=mat)
        >>> mt = MatrixTransform.transpose(rm)
        >>> mt.matrix[0]
        ['A', 'D']
        """
        transposed = list(map(list, zip(*matrix.matrix)))
        return RotationMatrix(base_sequence=matrix.base_sequence, matrix=transposed)

    @staticmethod
    def rotate_row_order(matrix: RotationMatrix, shift: int) -> RotationMatrix:
        """
        Reorders rows in the matrix by shifting their position.

        >>> base = ['A', 'B', 'C']
        >>> mat = [['A', 'B', 'C'], ['B', 'C', 'A'], ['C', 'A', 'B']]
        >>> rm = RotationMatrix(base_sequence=base, matrix=mat)
        >>> mt = MatrixTransform.rotate_row_order(rm, 1)
        >>> mt.matrix[0]
        ['C', 'A', 'B']
        """
        rows = matrix.matrix[-shift:] + matrix.matrix[:-shift]
        return RotationMatrix(base_sequence=matrix.base_sequence, matrix=rows)

    @staticmethod
    def rotate_column_order(matrix: RotationMatrix, shift: int) -> RotationMatrix:
        """
        Reorders columns in the matrix by shifting their position.

        >>> base = ['A', 'B', 'C']
        >>> mat = [['A', 'B', 'C'], ['C', 'B', 'A'], ['B', 'C', 'A']]
        >>> rm = RotationMatrix(base_sequence=base, matrix=mat)
        >>> mt = MatrixTransform.rotate_column_order(rm, 1)
        >>> mt.matrix[0]
        ['C', 'A', 'B']
        """
        num_cols = len(matrix.base_sequence)
        new_matrix = [row[-shift % num_cols:] + row[:-shift % num_cols] for row in matrix.matrix]
        return RotationMatrix(base_sequence=matrix.base_sequence, matrix=new_matrix)

