from typing import List

from utils.validators import ensure_not_empty


def shift_characters(chars: List[str], alphabet: List[str], shift: int) -> List[str]:
    """
    Apply modular index shift on characters within an alphabet.

    Args:
        chars: Input characters to shift.
        alphabet: Reference alphabet for index lookup.
        shift: Positions to shift (+ for encryption, - for decryption).

    Returns:
        List of shifted characters. Unknown symbols become '?'.
    """
    ensure_not_empty(chars)
    ensure_not_empty(alphabet)
    n = len(alphabet)

    return [
        alphabet[(alphabet.index(c) + shift) % n] if c in alphabet else '?'
        for c in chars
    ]


