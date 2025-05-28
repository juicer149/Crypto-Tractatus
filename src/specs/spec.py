from dataclasses import dataclass
from typing import Union, Optional, List
from specs.types import CipherType
from ciphers.base_cipher import CipherBit
from specs.registry import build_cipher

@dataclass
class CipherSpec:
    """
    A specification for a cipher, containing the type, text, alphabet, and optional keyword or shift.
    """

    type: CipherType
    text: str
    alphabet: Union[str, List[str]]
    keyword: Optional[str] = None
    shift: Optional[int] = None

    def to_cipher(self) -> CipherBit:
        return build_cipher(self)

