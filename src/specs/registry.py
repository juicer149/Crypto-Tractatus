from typing import Callable, Dict

from utils.error import InvalidCipherTypeError
from ciphers.base_cipher import CipherBit
from specs.spec import CipherSpec
from specs.types import CipherType

"""
This module provides a registry for cipher constructors, allowing for dynamic 
creation of cipher instances based on their specifications.
"""


CipherConstructor = Callable[[CipherSpec], CipherBit]

_registry: Dict[CipherType, CipherConstructor] = {}

def register_cipher(cipher_type: CipherType):
    def wrapper(func: CipherConstructor):
        _registry[cipher_type] = func
        return func
    return wrapper

def build_cipher(spec: CipherSpec) -> CipherBit:
    if spec.type not in _registry:
        raise InvalidCipherTypeError(f"Cipher type '{spec.type}' is not registered.")
    return _registry[spec.type](spec)

