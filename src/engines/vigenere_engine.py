from typing import List
from transforms.string_ops import split_text_to_chars
from transforms.list_ops import rotate
from transforms.mapping_ops import map_keys_to_values
from transforms.vigenere_rows import build_rotated_rows_from_keyword
from utils.validators import ensure_not_empty

def vigenere_encrypt_from_rows(text: str, keyword: str, alphabet: List[str]) -> List[str]:
    """
    Encrypts the input text using a prebuilt Vigenère row mapping.

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

    rows = build_rotated_rows_from_keyword(keyword, alphabet)
    table = map_keys_to_values(key_chars, *rows)

    key_iter = iter(key_chars)
    result = []

    for i, char in enumerate(text_chars):
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

