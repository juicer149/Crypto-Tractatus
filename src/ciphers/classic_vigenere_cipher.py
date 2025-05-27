from typing import List, Callable
from dataclasses import dataclass, field
from ciphers.base_cipher import CipherBit
from transforms.string_ops import split_text_to_chars
from transforms.list_ops import rotate_sequence_by_lookup_values, unique_preserve_order
from utils.validators import ensure_not_empty


@dataclass
class ClassicVigenereCipher(CipherBit):
    """
    Classic Vigenère cipher that operates on a list of characters using a keyword.

    Inherits from:
        CipherBit: Provides text and alphabet as character lists.

    Attributes:
        keyword (str): The encryption keyword.
        _key_chars (List[str]): Deduplicated characters from the keyword.
        _rotations (List[List[str]]): Rotated alphabets for each key character.
    """

    keyword: str
    _key_chars: List[str] = field(init=False)
    _rotations: List[List[str]] = field(init=False)

    def __post_init__(self):
        super().__post_init__()  # Calls CipherBit.__post_init__ to validate text/alphabet

        ensure_not_empty(self.keyword)
        raw_key = split_text_to_chars(self.keyword)
        self._key_chars = unique_preserve_order(raw_key)
        self._rotations = rotate_sequence_by_lookup_values(self._key_chars, self.alphabet)


    def __call__(self, mode: str = "encrypt") -> List[str]:
        return self.encrypt() if mode == "encrypt" else self.decrypt()


    def _run_cipher(self, lookup: Callable[[List[str], str], str]) -> List[str]:
        result = []
        key_index = 0

        for char in self.text:
            if char not in self.alphabet:
                result.append(char)
                continue

            key_char = self._key_chars[key_index % len(self._key_chars)]
            rotated_row = self._rotations[self._key_chars.index(key_char)]

            result.append(lookup(rotated_row, char))
            key_index += 1

        return result

    def encrypt(self) -> List[str]:
        return self._run_cipher(lambda row, char: row[self.alphabet.index(char)])

    def decrypt(self) -> List[str]:
        return self._run_cipher(lambda row, char: self.alphabet[row.index(char)] if char in row else '?')


