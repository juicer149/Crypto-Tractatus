from typing import List
from dataclasses import dataclass

from ciphers.base_cipher import CipherBit
from transforms.rot_ops import shift_characters
from structures.sequences import TextSequence, AlphabetSequence 


@dataclass
class RotCipher(CipherBit):
    shift: int

    def __post_init__(self):
        super().__post_init__()

    def __call__(self, mode: str = "encrypt") -> List[str]:
        return self.encrypt() if mode == "encrypt" else self.decrypt()

    def encrypt(self) -> List[str]:
        return shift_characters(self.text, self.alphabet, self.shift)

    def decrypt(self) -> List[str]:
        return shift_characters(self.text, self.alphabet, -self.shift)

