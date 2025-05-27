from transforms.list_ops import rotate_sequence_by_lookup_values

def build_rotated_rows_from_keyword(keyword: str, alphabet: List[str]) -> List[List[str]]:
    """
    Build a list of rotated alphabets in the order dictated by the keyword.

    Delegates the actual rotation logic to a reusable list transformation.

    Args:
        keyword: The key used to determine rotation patterns.
        alphabet: The base character set.

    Returns:
        A list of rotated rows corresponding to each character in the keyword.
    """
    ensure_not_empty(keyword)
    key_chars = split_text_to_chars(keyword)
    return rotate_sequence_by_lookup_values(key_chars, alphabet)

