import unittest
from transforms.rot_ops import rot_encrypt
from engines.vigenere_engine import classic_vigenere_encrypt

class TestCiphers(unittest.TestCase):

    def test_rot_encrypt(self):
        alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        text = "HELLO"
        shift = 3
        expected = list("KHOOR")
        result = rot_encrypt(text, shift, alphabet)
        self.assertEqual(result, expected)

    def test_vigenere_encrypt(self):
        alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        text = "HELLO"
        keyword = "KEY"
        expected = list("RIJVS")
        result = classic_vigenere_encrypt(text, keyword, alphabet)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
