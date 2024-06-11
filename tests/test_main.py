import unittest
import string
from src.main import add
from src.main import sha256
from src.main import generate_password

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

class TestGeneratePassword(unittest.TestCase):
    """
    Tests unitaires pour la fonction generate_password().
    """

    def test_password_length(self):
        """
        Teste que la fonction generate_password() renvoie un mot de passe dont la longueur est comprise entre 8 et 12 caractères.
        """
        password = generate_password()
        self.assertTrue(8 <= len(password) <= 12)

    def test_password_characters(self):
        """
        Teste que la fonction generate_password() renvoie un mot de passe contenant au moins une lettre minuscule, une lettre majuscule, un chiffre et un caractère de ponctuation.
        """
        password = generate_password()
        self.assertTrue(any(c.islower() for c in password))
        self.assertTrue(any(c.isupper() for c in password))
        self.assertTrue(any(c.isdigit() for c in password))
        self.assertTrue(any(c in string.punctuation for c in password))

if __name__ == '__main__':
    unittest.main()
