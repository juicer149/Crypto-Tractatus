from core.concept import CryptoConcept
from structures.alphabet import Alphabet
from structures.sequence import Sequence
from meta.registry import MappingMixin
from transforms.sequence_ops import SequenceTransform


def rot_transform(seq: Sequence[str], alphabet: Alphabet, shift: int) -> Sequence[str]:
    """
    Applies a rotation (ROT-N) cipher transformation to a sequence based on a given alphabet.

    This operation is purely functional and agnostic to the type of content in the sequence,
    as long as the characters exist in the alphabet.

    Args:
        seq: The sequence to transform.
        alphabet: The Alphabet used as rotation basis.
        shift: The shift amount (positive or negative).

    Returns:
        Transformed Sequence, where unknown symbols become '?'.

    Example:
        >>> from structures.alphabet import Alphabet
        >>> alpha = Alphabet.from_unicode_ranges("basic", [(65, 67)])  # ['A', 'B', 'C']
        >>> seq = Sequence(['A', 'B', 'C'])
        >>> rot_transform(seq, alpha, 1).data
        ['B', 'C', 'A']
    """
    rotated = SequenceTransform.rotate(alphabet.sequence.data, shift)
    mapping = MappingMixin()(alphabet.sequence.data, rotated)
    return Sequence([mapping.get(char, '?') for char in seq.data])


def make_rot_concept(alphabet: Alphabet, shift: int) -> CryptoConcept[str]:
    """
    Factory for creating a CryptoConcept representing a ROT transformation.

    Args:
        alphabet: Alphabet to use for mapping.
        shift: Shift amount.

    Returns:
        CryptoConcept wrapping a ROT-N transformation.

    Example:
        >>> from structures.alphabet import Alphabet
        >>> alpha = Alphabet.from_unicode_ranges("basic", [(65, 67)])  # ['A', 'B', 'C']
        >>> rot = make_rot_concept(alpha, shift=1)
        >>> rot(Sequence(['A', 'B', 'C'])).data
        ['B', 'C', 'A']
    """
    return CryptoConcept(
        name="ROT",
        family="transform",
        action=lambda seq: rot_transform(seq, alphabet, shift)
    )
