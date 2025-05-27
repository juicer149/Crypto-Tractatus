# src/utils/validators.py

from core.error import EmptySequenceError


def ensure_not_empty(seq, msg: str = "Cannot operate on empty sequence.") -> None:
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

# name before - ensure_positiv
def ensure_greater_then(
        n: int,
        threshold: int = 0,
        msg: str = "Value must be greater than threshold." 
        ) -> None:
    """
    Ensures that a given integer `n` is greater than `threshold`.

    Args:
        n: The number to validate.
        threshold: Minimum value `n` must exceed.
        msg: Custom error message.

    Raises:
        ValueError: If `n` is less than or equal to `threshold`.
    """
    if n <= threshold:
        raise ValueError(msg or f"Value must be greater than {threshold}.")


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

