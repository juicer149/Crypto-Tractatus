# src/transforms/string_ops.py

from typing import List
from transforms.list_ops import rotate
from utils.validators import ensure_not_empty


def split_text_to_chars(text: str) -> List[str]:
    """
    Split a string into a list of characters.

    Used to convert raw input into a character sequence suitable for transformation.

    Example:
        >>> split_text_to_chars("HELLO")
        ['H', 'E', 'L', 'L', 'O']
    """
    ensure_not_empty(text)
    return list(text)


def rot_text(text: str, shift: int, alphabet: List[str]) -> str:
    """
    Apply a Caesar-style rotation to a string using the given alphabet.

    Each character is shifted within the alphabet by `shift`.
    Characters not found in the alphabet are replaced with '?'.

    Example:
        >>> rot_text("ABC", 1, list("ABC"))
        'BCA'
    """
    ensure_not_empty(text)
    ensure_not_empty(alphabet)

    rotated = rotate(alphabet, shift)
    index_map = {char: idx for idx, char in enumerate(alphabet)}

    result = []
    for char in text:
        if char in index_map:
            idx = index_map[char]
            result.append(rotated[idx])
        else:
            result.append('?')
    return ''.join(result)

