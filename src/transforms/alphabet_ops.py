from typing import List, Tuple


def from_ascii_range(start: int, end: int) -> List[str]:
    """
    Generate a list of characters from an ASCII range.
    """
    if start > end:
        raise ValueError("Start must be less than or equal to end.")
    return [chr(c) for c in range(start, end + 1)]


def from_unicode_ranges(ranges: List[Tuple[int, int]]) -> List[str]:
    """
    Generate a list of characters from multiple Unicode ranges.
    """
    chars = []
    for start, end in ranges:
        chars.extend(chr(c) for c in range(start, end + 1))
    return chars


def from_string(s: str) -> List[str]:
    """
    Generate a list of characters from a string.
    """
    return list(s)


def with_extras(base: List[str], extras: List[str]) -> List[str]:
    """
    Combine a base list with extra characters, ensuring uniqueness.
    """
    seen = set(base)
    return base + [char for char in extras if char not in seen]

