from typing import Any

class CryptoTractatusError(Exception):
    """Bas-klass för alla anpassade fel i CryptoTractatus."""
    pass


class EmptySequenceError(CryptoTractatusError):
    """Raised when a sequence operation is attempted on an empty list."""
    def __init__(self, message="Cannot operate on an empty sequence."):
        super().__init__(message)


class DuplicateElementError(CryptoTractatusError):
    """Raised when a sequence is expected to be unique but isn't."""
    def __init__(self, message="Sequence contains duplicate elements."):
        super().__init__(message)


class InvalidRotationStepError(CryptoTractatusError):
    """Raised when a rotation step is zero or otherwise invalid."""
    def __init__(self, message="Rotation step must be non-zero."):
        super().__init__(message)


class InvalidCipherTypeError(CryptoTractatusError):
    """Raised when an invalid cipher type is specified."""
    def __init__(self, message="Invalid cipher type specified."):
        super().__init__(message)

class InvalidInputTypeError(CryptoTractatusError):
    def __init__(self, message: str):
        super().__init__(message)

class InvalidKeywordError(CryptoTractatusError):
    """Raised when an invalid keyword is used."""
    def __init__(self, message="Invalid keyword provided."):
        super().__init__(message)
