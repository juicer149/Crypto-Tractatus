from typing import List
from enum import Enum

CharList = List[str]

class CipherType(Enum):
    """Enumeration for different types of ciphers."""

    ROT = "rot"
    VIGENERE = "vigenere"
    CAESAR = "caesar"
