from typing import List, Union
from dataclasses import dataclass

from ciphers.base_cipher import CipherBit
from transforms.rot_ops import shift_characters


@dataclass  
class RotCipher(CipherBit):
    """
    A class to implement a ROT cipher, which shifts characters by a specified number.
    Attributes:
        text (str): The input text to be encrypted or decrypted.
        alphabet (Union[str, List[str]]): The alphabet used for the cipher.
        shift (int): The number of positions to shift each character.
    """

    shift: int


    def __call__(self, mode: str = "encrypt") -> List[str]:
        return self.encrypt() if mode == "encrypt" else self.decrypt()


    def encrypt(self) -> List[str]:
        return shift_characters(self.text, self.alphabet, self.shift)


    def decrypt(self) -> List[str]:
        return shift_characters(self.text, self.alphabet, -self.shift)

