# structures/sequences.py

from dataclasses import dataclass
from typing import List, Union, Iterator
from utils.coercion import coerce_to_char_list
from utils.validators import ensure_not_empty
from utils.error import InvalidKeywordError, DuplicateCharacterError
from transforms.list_ops import unique_preserve_order


@dataclass(frozen=True)
class SequenceBase:
    value: List[str]

    def __iter__(self) -> Iterator[str]:
        return iter(self.value)

    def __getitem__(self, index: int) -> str:
        return self.value[index]

    def __len__(self) -> int:
        return len(self.value)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, SequenceBase):
            return NotImplemented
        return self.value == other.value


@dataclass(frozen=True)
class TextSequence(SequenceBase):
    def __init__(self, raw: Union[str, List[str]]):
        coerced = coerce_to_char_list(raw)
        ensure_not_empty(coerced, "Text cannot be empty")
        object.__setattr__(self, "value", coerced)


@dataclass(frozen=True)
class AlphabetSequence(SequenceBase):
    def __init__(self, raw: Union[str, List[str]]):
        coerced = coerce_to_char_list(raw)
        ensure_not_empty(coerced, "Alphabet cannot be empty")

        if len(set(coerced)) != len(coerced):
            raise DuplicateCharacterError(f"Alphabet cannot contain duplicate characters (got: {coerced}).") 

        object.__setattr__(self, "value", coerced)


@dataclass(frozen=True)
class KeywordSequence(SequenceBase):
    def __init__(self, raw: Union[str, List[str]]):
        coerced = coerce_to_char_list(raw)
        ensure_not_empty(coerced, "Keyword cannot be empty")

        unique = unique_preserve_order(coerced)
        if len(unique) < 2:
            raise InvalidKeywordError(f"Keyword must contain at least two unique characters (got: {coerced}).")

        object.__setattr__(self, "value", unique)

