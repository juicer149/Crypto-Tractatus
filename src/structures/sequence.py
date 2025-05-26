# lib/sequences/sequence.py
from typing import List, TypeVar, Generic, Callable, Iterator
from dataclasses import dataclass
from  adapters.sequence_adapter import SequenceAdapter


T = TypeVar("T")


@dataclass(frozen=True)
class Sequence(Generic[T]):
    """
    Immutable, iterable sequence data container.

    Supports introspection, safe transformation, and semantic validation.

    Example:
        >>> s = Sequence(['A', 'B', 'C'])
        >>> 'B' in s
        True
        >>> s.index_of('C')
        2
    """

    data: List[T]


    def __getitem__(self, index):
        return self.data[index]


    def __len__(self):
        return len(self.data)


    def __iter__(self):
        return iter(self.data)


    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Sequence):
            return NotImplemented
        return self.data == other.data


    def __contains__(self, item: T) -> bool:
        return item in self.data


    def index_of(self, value: T) -> int:
        """
        Get index of a value.

        >>> s = Sequence(['A', 'B', 'C'])
        >>> s.index_of('B')
        1
        """
        
        return self.data.index(value)


    def validate_unique(self) -> None:
        """
        Raise ValueError if elements are not unique.

        >>> Sequence(['A', 'B', 'A']).validate_unique()
        Traceback (most recent call last):
            ...
        ValueError: Sequence contains duplicate values.
        """
        
        if len(set(self.data)) != len(self.data):
            raise ValueError("Sequence contains duplicate values.")


    def map(self, func: Callable[[T], T]) -> 'Sequence[T]':
        """
        Apply function to each element and return new sequence.

        >>> Sequence(['a', 'b']).map(str.upper)
        Sequence(data=['A', 'B'])
        """
        
        return Sequence([func(x) for x in self.data])


    def pipe(self, *functions: Callable[['Sequence[T]'], 'Sequence[T]']) -> 'Sequence[T]':
        """
        Apply a sequence of transformation functions to self.

        >>> s = Sequence(['A', 'B', 'C'])
        >>> s.pipe(lambda x: x.rotate(1)).data
        ['C', 'A', 'B']
        """
        
        result = self
        for fn in functions:
            result = fn(result)
        return result
