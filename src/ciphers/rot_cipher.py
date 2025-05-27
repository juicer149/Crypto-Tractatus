from typing import List, Union

from ciphers.base_cipher import CipherBit
from transforms.rot_ops import shift_characters


class RotCipher(CipherBit):

    def __init__(self, text: Union[str, List[str]], alphabet: List[str], shift: int):
        super().__init__(text, alphabet)
        self.shift = shift


    def __call__(self, mode: str = "encrypt") -> List[str]:
        return self.encrypt() if mode == "encrypt" else self.decrypt()


    def encrypt(self) -> List[str]:
        return shift_characters(self.text, self.alphabet, self.shift)


    def decrypt(self) -> List[str]:
        return shift_characters(self.text, self.alphabet, -self.shift)

