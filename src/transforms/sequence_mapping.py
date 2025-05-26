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

