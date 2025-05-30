from abc import ABC, abstractmethod
from typing import List
from dataclasses import dataclass
from utils.validators import ensure_not_empty

@dataclass
class CipherBit(ABC):
    text: List[str]
    alphabet: List[str]

    def __post_init__(self):
        ensure_not_empty(self.text, "Text must not be empty.")
        ensure_not_empty(self.alphabet, "Alphabet must not be empty.")

    @abstractmethod
    def encrypt(self) -> List[str]:
        pass

    @abstractmethod
    def decrypt(self) -> List[str]:
        pass

