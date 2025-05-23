from abc import ABC, abstractmethod
from typing import NamedTuple, Set

class CipherResult(NamedTuple):
    output: str
    unknown: Set[str]

class BaseEngine(ABC):
    """
    Abstract base class for all cipher engines.

    Each engine must implement a __call__ method that takes a text input
    and required keyword arguments (e.g., shift, key, alphabet),
    and returns a CipherResult with the transformed output and
    a set of unknown characters encountered.
    """

    @abstractmethod
    def __call__(self, text: str, **kwargs) -> CipherResult:
        ...
