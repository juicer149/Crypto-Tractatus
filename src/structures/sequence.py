# lib/sequences/sequence.py
from typing import List, TypeVar, Generic, Callable, Iterator
from dataclasses import dataclass
from .sequence_transform import SequenceTransform


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


    def rotate(self, shift: int) -> 'Sequence[T]':
        """
        Rotate sequence by shift (positive or negative).

        >>> Sequence(['A', 'B', 'C']).rotate(1)
        Sequence(data=['C', 'A', 'B'])
        """
        
        return Sequence(SequenceTransform.rotate(self.data, shift))


    def move_to_front(self, elements: List[T]) -> Iterator['Sequence[T]']:
        """
        Yield variants with specified elements moved to front.

        >>> list(Sequence(['A', 'B', 'C']).move_to_front(['C']))
        [Sequence(data=['C', 'A', 'B'])]
        """

        for variant in SequenceTransform.move_elements_to_front(self.data, elements):
            yield Sequence(variant)

