from typing import List, Callable
from dataclasses import dataclass, field

from ciphers.base_cipher import CipherBit
from transforms.list_ops import rotate_sequence_by_lookup_values
from structures.sequences import KeywordSequence, AlphabetSequence


@dataclass
class ClassicVigenereCipher(CipherBit):
    keyword: KeywordSequence
    _key_chars: List[str] = field(init=False)
    _rotations: List[List[str]] = field(init=False)

    def __post_init__(self):
        super().__post_init__()
        self._key_chars = list(self.keyword)
        self._rotations = rotate_sequence_by_lookup_values(self._key_chars, list(self.alphabet))

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
        return self._run_cipher(lambda row, char: self.alphabet[self.alphabet.index(char)] if char in row else '?')

