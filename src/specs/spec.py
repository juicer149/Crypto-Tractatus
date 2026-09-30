from dataclasses import dataclass
from typing import List, Optional, Union

from specs.types import CipherType


@dataclass
class CipherSpec:
    """
    Specification for constructing a cipher.
    """

    type: CipherType
    text: str
    alphabet: Union[str, List[str]]
    keyword: Optional[str] = None
    shift: Optional[int] = None

    def to_cipher(self):
        from specs.registry import build_cipher

        return build_cipher(self)
