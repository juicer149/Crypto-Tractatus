from typing import List, Dict, Any, Callable, Iterator, Union

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


def map_keys_to_values(keys: List[Any], *value_lists: List[Any], warn: bool = True) -> Dict[Any, Union[Any, List[Any]]]:
    """
    Map keys to one or more value lists. 
    If one list is provided, map key to single value. If multiple, map key to list of values.

    Args:
        keys: List of keys.
        *value_lists: Value lists to associate per key.
        warn: Whether to issue warning on length mismatch.

    Returns:
        Dict mapping each key to value or list of values.

    Example:
        >>> map_keys_to_values(['A', 'B'], ['C', 'D'])
        {'A': 'C', 'B': 'D'}
        >>> map_keys_to_values(['A', 'B'], ['C', 'D'], ['E', 'F'])
        {'A': ['C', 'E'], 'B': ['D', 'F']}
    """
    single = len(value_lists) == 1
    max_len = max(len(keys), *(len(v) for v in value_lists))
    result = {}

    for i, key in enumerate(keys):
        values = []
        for vlist in value_lists:
            if i < len(vlist):
                values.append(vlist[i])
            else:
                if warn:
                    warnings.warn(f"Value list shorter than keys at index {i}")
                values.append(None)

        result[key] = values[0] if single else values

    return result
