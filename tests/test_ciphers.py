import unittest

from ciphers.classic_vigenere_cipher import ClassicVigenereCipher
from ciphers.rot_cipher import RotCipher
from structures.sequences import KeywordSequence


ALPHABET = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")


class TestCiphers(unittest.TestCase):
    def test_rot_encrypt(self):
        cipher = RotCipher(
            text=list("HELLO"),
            alphabet=ALPHABET,
            shift=3,
        )

        self.assertEqual(cipher.encrypt(), list("KHOOR"))

    def test_rot_round_trip(self):
        encrypted = RotCipher(
            text=list("HELLO"),
            alphabet=ALPHABET,
            shift=3,
        ).encrypt()

        decrypted = RotCipher(
            text=encrypted,
            alphabet=ALPHABET,
            shift=3,
        ).decrypt()

        self.assertEqual(decrypted, list("HELLO"))

    def test_vigenere_encrypt(self):
        cipher = ClassicVigenereCipher(
            text=list("HELLO"),
            alphabet=ALPHABET,
            keyword=KeywordSequence("KEY"),
        )

        self.assertEqual(cipher.encrypt(), list("RIJVS"))

    def test_vigenere_round_trip(self):
        encrypted = ClassicVigenereCipher(
            text=list("HELLO"),
            alphabet=ALPHABET,
            keyword=KeywordSequence("KEY"),
        ).encrypt()

        decrypted = ClassicVigenereCipher(
            text=encrypted,
            alphabet=ALPHABET,
            keyword=KeywordSequence("KEY"),
        ).decrypt()

        self.assertEqual(decrypted, list("HELLO"))

    def test_vigenere_preserves_repeated_keyword_characters(self):
        keyword = KeywordSequence("BOOK")

        self.assertEqual(list(keyword), list("BOOK"))

        encrypted = ClassicVigenereCipher(
            text=list("HELLO"),
            alphabet=ALPHABET,
            keyword=keyword,
        ).encrypt()

        decrypted = ClassicVigenereCipher(
            text=encrypted,
            alphabet=ALPHABET,
            keyword=keyword,
        ).decrypt()

        self.assertEqual(decrypted, list("HELLO"))


if __name__ == "__main__":
    unittest.main()
