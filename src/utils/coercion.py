from typing import Any, List, TypeVar, Callable, Union, Optional
from utils.error import InvalidInputTypeError, InvalidKeywordError


T = TypeVar("T")

def coerce_to_list(data: Any) -> List[Any]:
    """
    Ensure the input is a non-empty list. Convert string to list of characters.
    Leave other iterables unchanged.

    Returns:
        A list of elements from the input.
    """
    if isinstance(data, list):
        result = data
    elif isinstance(data, str):
        result = list(data)
    elif hasattr(data, "__iter__"):
        result = list(data)
    else:
        raise InvalidInputTypeError(f"Cannot coerce type {type(data).__name__} to list.")
    
    return result


def coerce_to_char_list(data: Union[str, List[str]]) -> List[str]:
    """
    Ensure input is a non-empty list of characters.
    If a string is provided, convert to list of characters.
    """
    if isinstance(data, str):
        result = list(data)
    elif isinstance(data, list) and all(isinstance(el, str) for el in data):
        result = data
    else:
        raise InvalidInputTypeError(f"Expected str or List[str], but got {type(data).__name__}: {data!r}")

    return result

def generate_coerced_fields(
    text: Union[str, List[str]],
    alphabet: Union[str, List[str]],
    keyword: Optional[Union[str, List[str]]] = None,
    require_keyword: bool = False
) -> tuple[List[str], List[str], Optional[List[str]]]:
    """
    Convert inputs to lists of characters, validate non-emptiness,
    and handle optional keyword based on requirement.
    """
    coerced_text = coerce_to_char_list(text)
    coerced_alphabet = coerce_to_char_list(alphabet)

    keyword = keyword or "" # Default to empty string if None
    
    if require_keyword and not keyword:
        raise InvalidKeywordError("Keyword is required but not provided.")

    coerced_keyword = coerce_to_char_list(keyword)  # Ensure keyword is a list of characters if provided 

    return coerced_text, coerced_alphabet, coerced_keyword


def apply_transformations(
    data: dict[str, Any],
    transformations: dict[str, Callable[[Any], Any]]
) -> dict[str, Any]:
    """
    Apply a transformation function to specified fields in a dictionary.

    Args:
        data: A dictionary of data to transform.
        transformations: A dictionary mapping keys to transformation functions.

    Returns:
        A new dictionary with the transformations applied.
    """
    return {
        key: transformations[key](value) if key in transformations else value
        for key, value in data.items()
    }
