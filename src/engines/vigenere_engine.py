from typing import List, Dict
from transforms.vigenere_rows import build_rotated_rows_from_keyword
from transforms.mapping_ops import map_keys_to_values
from transforms.string_ops import split_text_to_chars
from utils.validators import ensure_not_empty

def classic_vigenere_encrypt(text: str, keyword: str, alphabet: List[str]) -> List[str]:
    """
    Encrypts the input text using the classic Vigenère cipher method.

    Args:
        text: The input string to encrypt.
        keyword: The keyword guiding the row order.
        alphabet: The base alphabet used to construct rotations.

    Returns:
        A list of encrypted characters.
    """
    ensure_not_empty(text)
    ensure_not_empty(keyword)

    key_chars = split_text_to_chars(keyword)
    text_chars = split_text_to_chars(text)

    # Build the rotation table once per key character
    rows = build_rotated_rows_from_keyword(keyword, alphabet)
    table = map_keys_to_values(key_chars, *rows)

    key_iter = iter(key_chars)
    result = []

    for char in text_chars:
        try:
            key = next(key_iter)
        except StopIteration:
            key_iter = iter(key_chars)
            key = next(key_iter)

        if char not in alphabet:
            result.append('?')
        else:
            cipher_row = table.get(key, alphabet)
            result.append(cipher_row[alphabet.index(char)])

    return result

