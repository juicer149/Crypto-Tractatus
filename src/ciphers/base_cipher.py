from abc import ABC, abstractmethod
from typing import List, Union
from dataclasses import dataclass

from transforms.string_ops import split_text_to_chars
from utils.validators import ensure_not_empty


@dataclass
class CipherBit(ABC):
    """
    Base class for cipher bits, defining the structure for encryption and decryption methods.

    Attributes:
        text (Union[str, List[str]]): The text to be encrypted or decrypted.
        alphabet (List[str]): The alphabet used for encryption and decryption.
    """
    
    text: Union[str, List[str]]
    alphabet: List[str]


    def __post_init__(self):
        """Post-initialization to ensure text is in the correct format and not empty."""

        if isinstance(self.text, str):
            self.text = split_text_to_chars(self.text)
        
        ensure_not_empty(self.text)
        ensure_not_empty(self.alphabet)


    @abstractmethod
    def encrypt(self) -> List[str]:
        pass


    @abstractmethod
    def decrypt(self) -> List[str]:
        pass

