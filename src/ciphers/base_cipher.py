from abc import ABC, abstractmethod
from typing import List
from dataclasses import dataclass

from utils.validators import ensure_not_empty


@dataclass
class CipherBit(ABC):
    """
    Base class for cipher bits, defining the structure for encryption and decryption methods.

    Attributes:
        text (Union[str, List[str]]): The text to be encrypted or decrypted.
        alphabet (List[str]): The alphabet used for encryption and decryption.
    """
    
    text: List[str]
    alphabet: List[str]


    def __post_init__(self):
        """Post-initialization to ensure text is in the correct format and not empty."""
        
        ensure_not_empty(self.text, "Text must not be empty.")
        ensure_not_empty(self.alphabet, "Alphabet must not be empty.")


    @abstractmethod
    def encrypt(self) -> List[str]:
        pass


    @abstractmethod
    def decrypt(self) -> List[str]:
        pass

