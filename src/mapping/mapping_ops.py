from typing import List, Dict, Any
import warnings

def build_char_mapping(
    base: List[str],
    generator_func: Callable[[List[str], int], Iterator[List[str]]],
    step: int = 1
) -> dict[str, List[str]]:
    """
    Build a character-to-sequence mapping from a base list and a generator.

    Args:
        base: Base character sequence (e.g. alphabet).
        generator_func: A generator function that produces a series of derived lists.
        step: Step or parameter passed into the generator (default = 1).

    Returns:
        Dictionary mapping each base character to a generated list.

    Example:
        >>> from transforms.list_ops import rotate_generator
        >>> base = ['A', 'B', 'C']
        >>> build_char_mapping(base, rotate_generator, step=1)
        {'A': ['A', 'B', 'C'], 'B': ['C', 'A', 'B'], 'C': ['B', 'C', 'A']}
    """
    generated = list(generator_func(base, step))
    return map_keys_to_values(base, *generated)


def map_keys_to_values(keys: List[Any], *value_lists: List[Any], warn: bool = True) -> Dict[Any, List[Any]]:
    """
    Creates a mapping from keys to zipped value lists.

    This is useful for representing relation tables (e.g., Vigenère or Enigma)
    where one list acts as a header or row identifier, and the others provide
    corresponding values.

    If the lengths mismatch, missing values are filled with None, and optionally a warning is issued.

    Args:
        keys: The primary list to use as dict keys.
        *value_lists: One or more value lists to be zipped per key.
        warn: Whether to issue a warning if lists differ in length.

    Returns:
        A dictionary mapping each key to a list of associated values.

    Example:
        >>> map_keys_to_values(['A', 'B'], ['C', 'D'], ['E', 'F'])
        {'A': ['C', 'E'], 'B': ['D', 'F']}
    """
    max_len = max(len(keys), *(len(v) for v in value_lists))
    result = {}

    for i, key in enumerate(keys):
        mapped = []
        for value_list in value_lists:
            if i < len(value_list):
                mapped.append(value_list[i])
            else:
                if warn:
                    warnings.warn(f"Value list shorter than keys at index {i}")
                mapped.append(None)
        result[key] = mapped

    return result
