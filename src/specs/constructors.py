from specs.registry import register_cipher
from specs.types import CipherType
from specs.spec import CipherSpec
from ciphers.rot_cipher import RotCipher
from ciphers.classic_vigenere_cipher import ClassicVigenereCipher
from ciphers.base_cipher import CipherBit
from math.sequence_math import unique_rotation
from utils.error import InvalidRotationStepError, InvalidKeywordError
from structures.sequences import TextSequence, AlphabetSequence, KeywordSequence


@register_cipher(CipherType.ROT)
def rot_constructor(spec: CipherSpec) -> CipherBit:
    if spec.shift is None:
        raise InvalidRotationStepError(f"Shift must be specified for ROT cipher (got {spec.shift}).")

    text = TextSequence(spec.text)
    alphabet = AlphabetSequence(spec.alphabet)

    if unique_rotation(spec.shift, len(alphabet)) == 1:
        raise InvalidRotationStepError(
            f"Shift {spec.shift} produces no effective rotation for alphabet of length {len(alphabet)}."
        )

    return RotCipher(text=list(text), alphabet=list(alphabet), shift=spec.shift)


@register_cipher(CipherType.VIGENERE)
def vigenere_constructor(spec: CipherSpec) -> CipherBit:
    if spec.keyword is None:
        raise InvalidKeywordError("Keyword must be provided for Vigenère cipher.")

    text = TextSequence(spec.text)
    alphabet = AlphabetSequence(spec.alphabet)
    keyword = KeywordSequence(spec.keyword)

    return ClassicVigenereCipher(
        text=list(text),
        alphabet=list(alphabet),
        keyword=keyword
    )

