# lib/sequences/math.py
from typing import Dict
from math import gcd

from utils.validators import ensure_greater_then, ensure_not_equal

"""
Mathematical utility for analyzing step-based rotations of sequences.
"""


def normalize_shift(shift: int, length: int) -> int:
    """
    Normalize shift to be within sequence bounds.

    >>> SequenceMath.normalize_shift(4, 3)
    1
    >>> SequenceMath.normalize_shift(-2, 3)
    -2
    """
    ensure_greater_then(length, 0, "Length must be greater than 0.")
    return shift % length if shift >= 0 else -(abs(shift) % length)


def unique_rotation(step: int, length: int) -> int:
    """
    Number of unique positions visited with a given step.

    >>> SequenceMath.unique_rotation(10, 3)
    10
    >>> SequenceMath.unique_rotation(6, 2)
    3
    """
    # byt mot validator
    ensure_greater_then(length, 0, "Length must be greater than 0.")
    ensure_not_equal(step, 0, "Step must not be zero.")

    return length // gcd(abs(step), length)



def valid_rotations(length: int) -> Dict[int, int]:
    """
    Return a map of all valid step sizes and their cycle lengths.

    >>> SequenceMath.valid_rotations(6)
    {1: 6, 2: 3, 3: 2, 4: 3, 5: 6}
    """
    ensure_greater_then(length, 0, "Length must be greater than 0.")
    return {step: unique_rotation(length, step) for step in range(1, length)}

