# lib/sequences/math.py
from typing import Dict
from math import gcd


class SequenceMath:
    """
    Mathematical utility for analyzing step-based rotations of sequences.
    """


    @staticmethod
    def normalize_shift(shift: int, length: int) -> int:
        """
        Normalize shift to be within sequence bounds.

        >>> SequenceMath.normalize_shift(4, 3)
        1
        >>> SequenceMath.normalize_shift(-2, 3)
        -2
        """
        
        if length <= 0:
            raise ValueError("Length must be positive.")
        return shift % length if shift >= 0 else -(abs(shift) % length)


    @staticmethod
    def unique_rotation(length: int, step: int) -> int:
        """
        Number of unique positions visited with a given step.

        >>> SequenceMath.unique_rotation(10, 3)
        10
        >>> SequenceMath.unique_rotation(6, 2)
        3
        """
        
        if length <= 0 or step == 0:
            raise ValueError("Invalid input.")
        return length // gcd(abs(step), length)


    @staticmethod
    def valid_rotations(length: int) -> Dict[int, int]:
        """
        Return a map of all valid step sizes and their cycle lengths.

        >>> SequenceMath.valid_rotations(6)
        {1: 6, 2: 3, 3: 2, 4: 3, 5: 6}
        """
        
        if length <= 0:
            raise ValueError("Invalid input.")
        return {step: SequenceMath.unique_rotation(length, step) for step in range(1, length)}

