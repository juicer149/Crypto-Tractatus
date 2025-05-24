# src/utils/validators.py

from core.error import EmptySequenceError


def ensure_non_empty(seq, msg: str = "Cannot operate on empty sequence.") -> None:
    """
    Raise an error if the sequence is empty.

    Args:
        seq: A list-like structure to check.
        msg: Optional custom error message.

    Raises:
        EmptySequenceError: If the sequence is empty.
    """
    if not seq:
        raise EmptySequenceError(msg)


def ensure_positive(n: int, msg: str = "Value must be positive.") -> None:
    """
    Raise an error if the number is zero or negative.

    Args:
        n: Integer to check.
        msg: Optional custom error message.

    Raises:
        ValueError: If n <= 0.
    """
    if n <= 0:
        raise ValueError(msg)


def ensure_not_equal(n: int, disallowed: int, msg: str = "Value must not be equal to disallowed.") -> None:
    """
    Raise an error if a number is equal to a disallowed value.

    Args:
        n: Number to check.
        disallowed: Value n must not be equal to.
        msg: Optional custom error message.

    Raises:
        ValueError: If n == disallowed.
    """
    if n == disallowed:
        raise ValueError(msg)

