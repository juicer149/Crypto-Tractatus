from typing import Callable, List

from structures.sequence import Sequence
from structures.rotation_table import RotationTable
from core.concept import CryptoConcept
from structures.alphabet import Alphabet
from structures.rotation_table import RotationTable
from lib.multi.vigenere_tables import build_vigenere_tables  # din nya modul
from strategies.strategies import round_robin_strategy, pattern_strategy, static_strategy
from lib.multi.vigenere_multi import vigenere_transform_multi  # krypteraren

def vigenere_transform_multi(
    seq: Sequence[str],
    key: str,
    tables: Dict[int, RotationTable],
    strategy: Callable[[int, int], int]
) -> Sequence[str]:
    """
    Applies Vigenère encryption using multiple rotation tables and an alternation strategy.

    Args:
        seq: The input sequence.
        key: Key used for lookup in the tables.
        tables: Dictionary of indexed RotationTables.
        strategy: Function to determine which table to use at each position.

    Returns:
        Encrypted Sequence.

    Example:
        >>> from structures.alphabet import Alphabet
        >>> alpha = Alphabet.from_unicode_ranges("basic", [(65, 67)])
        >>> tables = build_vigenere_tables(["A", "B"], alpha)
        >>> vigenere_transform_multi(Sequence(['A', 'B', 'C']), key="B", tables=tables, strategy=round_robin_strategy).data
        ['B', 'C', 'A']
    """
    output = []
    table_count = len(tables)

    key_cycle = (k for k in key)

    for i, char in enumerate(seq.data):
        idx = strategy(i, table_count)
        table = tables[idx]

        try:
            k = next(key_cycle)
        except StopIteration:
            key_cycle = (k for k in key)
            k = next(key_cycle)

        if k not in table.base.sequence or char not in table.base.sequence:
            output.append('?')
            continue

        output.append(table.lookup(plain=char, key=k))

    return Sequence(output)


def make_multi_vigenere_concept(
    keys: List[str],
    alphabet: Alphabet,
    strategy: Callable[[int, int], int] = round_robin_strategy,
    step: int = 1,
    mode: str = "normal",
    shuffle: bool = False
) -> CryptoConcept[str]:
    """
    Factory for creating a CryptoConcept that encrypts using multiple Vigenère tables
    and a user-defined alternation strategy.

    Args:
        keys: List of key strings.
        alphabet: Base Alphabet object.
        strategy: Function deciding which table to use per position.
        step: Rotation step in table generation.
        mode: "normal" or "mirror".
        shuffle: Whether to shuffle the alphabet before building each table.

    Returns:
        A CryptoConcept that can be called on a Sequence[str].

    Example:
        >>> from structures.alphabet import Alphabet
        >>> alpha = Alphabet.from_unicode_ranges("basic", [(65, 67)])
        >>> concept = make_multi_vigenere_concept(["DOG", "CAT"], alpha)
        >>> concept(Sequence(['A', 'B', 'C'])).data  # Encrypted output
        ['H', 'F', 'D']
    """
    tables: dict[int, RotationTable] = build_vigenere_tables(
        keys=keys,
        alphabet=alphabet,
        step=step,
        mode=mode,
        shuffle=shuffle
    )

    def action(seq: Sequence[str]) -> Sequence[str]:
        # Nyckeln används som concatenation av alla keys – kan också göras alternativt
        merged_key = ''.join(keys)
        return vigenere_transform_multi(seq, key=merged_key, tables=tables, strategy=strategy)

    return CryptoConcept(
        name="MULTI_VIGENERE",
        family="engine",
        action=action
    )
