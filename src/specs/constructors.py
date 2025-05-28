# specs/constructors.py
# specs/constructors.py

from specs.registry import register_cipher
from specs.types import CipherType
from specs.spec import CipherSpec
from ciphers.rot_cipher import RotCipher
from ciphers.classic_vigenere_cipher import ClassicVigenereCipher
from ciphers.base_cipher import CipherBit
from utils.coercion import generate_coerced_fields
from math.sequence_math import unique_rotation
from utils.error import InvalidRotationStepError, InvalidKeywordError


@register_cipher(CipherType.ROT)
def rot_constructor(spec: CipherSpec) -> CipherBit:
    if spec.shift is None:
        raise InvalidRotationStepError(f"Shift must be specified for ROT cipher, (got {spec.shift}).")

    text, alphabet, _ = generate_coerced_fields(spec.text, spec.alphabet)

    if unique_rotation(spec.shift, len(alphabet)) == 1:
        raise InvalidRotationStepError(
            f"Shift {spec.shift} produces no effective rotation for alphabet of length {len(alphabet)}."
        )

    return RotCipher(text=text, alphabet=alphabet, shift=spec.shift)


@register_cipher(CipherType.VIGENERE)
def vigenere_constructor(spec: CipherSpec) -> CipherBit:
    text, alphabet, keyword = generate_coerced_fields(
        spec.text, spec.alphabet, spec.keyword, require_keyword=True
    )

    if not keyword or len(set(keyword)) < 2:
        raise InvalidKeywordError(f"Keyword must be a non-empty string with at least two unique characters (got '{keyword}').")

    return ClassicVigenereCipher(
        text=text,
        alphabet=alphabet,
        keyword=keyword
    )
