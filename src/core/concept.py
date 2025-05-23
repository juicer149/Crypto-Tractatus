from typing import Callable, Generic, TypeVar, Dict, Any
from structures.sequence import Sequence

T = TypeVar('T')


class ConceptualError(Exception):
    """
    Raised when two CryptoConcepts cannot be meaningfully combined.

    Example:
        >>> raise ConceptualError("ROT and Vigenere are semantically incompatible.")
        Traceback (most recent call last):
        ...
        ConceptualError: ROT and Vigenere are semantically incompatible.
    """
    pass


T = TypeVar('T')


class CryptoConcept(Generic[T]):
    """
    Represents a semantically annotated transformation on a Sequence.

    Attributes:
        name (str): Identifier for the concept.
        family (str): Semantic group the concept belongs to.
        action (Callable): Callable transformation.
    """

    def __init__(self, name: str, family: str, action: Callable[[Sequence[T]], Sequence[T]]):
        self.name = name
        self.family = family
        self.action = action
        self._meta: Dict[str, Any] = {}

    def __call__(self, sequence: Sequence[T]) -> Sequence[T]:
        return self.action(sequence)

    def __repr__(self):
        return f"<CryptoConcept name={self.name} family={self.family}>"

    def set_meta(self, key: str, value: Any) -> None:
        """
        Sets a metadata field.

        >>> c = CryptoConcept("ROT", "transform", lambda s: s)
        >>> c.set_meta("shift", 3)
        >>> c.meta("shift")
        3
        """
        self._meta[key] = value

    def meta(self, key: str) -> Any:
        """
        Retrieves a metadata value by key.

        Raises:
            KeyError: if key is not present.

        >>> c = CryptoConcept("ROT", "transform", lambda s: s)
        >>> c.set_meta("shift", 3)
        >>> c.meta("shift")
        3
        """
        if key not in self._meta:
            raise KeyError(f"Metadata key '{key}' not found in concept '{self.name}'")
        return self._meta[key]

    def has_meta(self, key: str) -> bool:
        """
        Checks if a metadata key exists.

        >>> c = CryptoConcept("ROT", "transform", lambda s: s)
        >>> c.has_meta("foo")
        False
        """
        return key in self._meta



def combine(a: CryptoConcept, b: CryptoConcept) -> CryptoConcept:
    """
    Attempts to semantically compose two CryptoConcepts.

    Special case: VIGENERE + VIGENERE → MULTI_VIGENERE with round-robin logic.

    Raises:
        ConceptualError if combination is invalid.

    Example:
        >>> from structures.sequence import Sequence
        >>> rot = CryptoConcept("ROT", "transform", lambda s: s)
        >>> mirror = CryptoConcept("MIRROR", "transform", lambda s: Sequence(list(reversed(s.data))))
        >>> combine(rot, mirror).name
        'ROT_MIRROR'
    """
    # VIGENERE + VIGENERE → Alternating/Multi-Vigenère
    if a.family == b.family == "engine" and a.name == "VIGENERE" and b.name == "VIGENERE":
        try:
            key_a = a._meta["key"]
            key_b = b._meta["key"]
            alphabet = a._meta["alphabet"]
        except (AttributeError, KeyError):
            raise ConceptualError("Cannot combine Vigenère engines without metadata (key, alphabet).")

        from ciphers.multi_vigenere_cipher import make_multi_vigenere_concept
        return make_multi_vigenere_concept(
            keys=[key_a, key_b],
            alphabet=alphabet,
            strategy=round_robin_strategy  # Standard
        )

    if a.family == b.family:
        if a.name == "ROT" and b.name == "ROT":
            raise NotImplementedError("ROT + ROT combination should sum shifts explicitly.")
        else:
            raise ConceptualError(f"Filosofisk förvirring: '{a.name}' och '{b.name}' tillhör båda '{a.family}'")

    def composed(seq):
        return b(a(seq))

    return CryptoConcept(name=f"{a.name}_{b.name}", family="composite", action=composed)

