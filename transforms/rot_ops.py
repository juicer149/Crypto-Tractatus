from typing import List
from transforms.list_ops import rotate
from mapping.mapping_ops import map_keys_to_values

def rot_encrypt(text: str, shift: int, alphabet: List[str]) -> List[str]:
    """
    Encrypts the text using ROT cipher with a given shift and alphabet.

    Args:
        text: The input text to encrypt.
        shift: The number of positions to shift each character.
        alphabet: The list of characters representing the alphabet.

    Returns:
        A list of encrypted characters.
    """
    # Create a mapping of each character to its rotated equivalent
    rotated_alphabet = rotate(alphabet, shift)
    char_map = map_keys_to_values(alphabet, rotated_alphabet)

    # Encrypt the text using the character map
    encrypted_text = [char_map.get(char, char) for char in text]
    return encrypted_text
