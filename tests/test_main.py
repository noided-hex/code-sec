import unittest
from src.main import add
from src.main import sha256

class TestMain(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 4), 6)
        self.assertEqual(add(-1, 3), 2)
        self.assertEqual(add(-1, -2), -3)

    def test_sha256_empty_string(self):
        """
        Teste que la fonction sha256() renvoie la bonne empreinte pour une chaîne de caractères vide.
        """
        self.assertEqual(sha256(""), "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855")

    def test_sha256_hello_world(self):
        """
        Teste que la fonction sha256() renvoie la bonne empreinte pour la chaîne de caractères "hello world".
        """
        self.assertEqual(sha256("hello world"), "b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9")

if __name__ == '__main__':
    unittest.main()
