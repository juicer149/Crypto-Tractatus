
from typing import Dict

from structures.alphabet import Alphabet
from structures.rotation_table import RotationTable
from core.concept import CryptoConcept
from structures.sequence import Sequence
from ciphers.vigenere_cipher import vigenere_transform


def build_vigenere_tables(
    keys: list[str],
    alphabet: Alphabet,
    step: int = 1,
    mode: str = "normal",
    shuffle: bool = False
) -> Dict[int, RotationTable]:
    """
    Generate multiple RotationTables for a set of Vigenère keys.

    Args:
        keys: List of keys (e.g. ["DOG", "BONE"]).
        alphabet: Base alphabet.
        step: Rotation step for the tables.
        mode: "normal" or "mirror".
        shuffle: If True, shuffles the alphabet for each table.

    Returns:
        Dictionary of indexed RotationTables.

    Example:
        >>> from structures.alphabet import Alphabet
        >>> alpha = Alphabet.from_unicode_ranges("basic", [(65, 67)])
        >>> tables = build_vigenere_tables(["A", "B"], alpha)
        >>> len(tables)
        2
    """
    from copy import deepcopy
    from random import shuffle as rand_shuffle
    from structures.sequence import Sequence

    tables = {}
    for i, key in enumerate(keys):
        data = deepcopy(alphabet.sequence.data)
        if shuffle:
            rand_shuffle(data)
        if mode == "mirror":
            data = list(reversed(data))
        custom_alpha = Alphabet(name=f"{alphabet.name}_k{i}", sequence=Sequence(data))
        tables[i] = RotationTable(custom_alpha, step=step, mode="normal")  # 'mode' is already mirrored above
    return tables


def make_vigenere_concept(
    alphabet: Alphabet,
    key: str,
    step: int = 1,
    mode: str = "normal",
    shuffle_alphabet: bool = False
) -> CryptoConcept[str]:
    """
    Factory for creating a CryptoConcept representing a Vigenère cipher transformation.

    Args:
        alphabet: Alphabet for encryption.
        key: Key string for cipher.
        step: Step size for internal rotation table.
        mode: "normal" or "mirror" for direction of rotation.
        shuffle_alphabet: If True, randomizes the alphabet order.

    Returns:
        A CryptoConcept ready for composition and execution.

    Example:
        >>> from structures.alphabet import Alphabet
        >>> alpha = Alphabet.from_unicode_ranges("basic", [(65, 67)])  # ['A', 'B', 'C']
        >>> vigenere = make_vigenere_concept(alpha, key="B")
        >>> vigenere(Sequence(['A', 'B', 'C'])).data
        ['B', 'C', 'A']
    """
    concept = CryptoConcept(
        name="VIGENERE",
        family="engine",
        action=lambda seq: vigenere_transform(
            seq, key=key, alphabet=alphabet, step=step, mode=mode, shuffle_alphabet=shuffle_alphabet
        )
    )
    concept._meta = {
        "key": key,
        "alphabet": alphabet,
        "step": step,
        "mode": mode,
        "shuffle_alphabet": shuffle_alphabet
    }
    return concept
