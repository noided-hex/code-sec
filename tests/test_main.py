import unittest
import string
import os
import json
from src.main import add
from src.main import sha256
from src.main import generate_password
from src.main import save_password_hash


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
        Teste que la fonction generate_password() renvoie un mot de passe dont la longueur est comprise entre 8 
        et 12 caractères.
        """
        password = generate_password()
        self.assertTrue(8 <= len(password) <= 12)

    def test_password_characters(self):
        """
        Teste que la fonction generate_password() renvoie un mot de passe contenant au moins une lettre minuscule,
        une lettre majuscule, un chiffre et un caractère de ponctuation.
        """
        password = generate_password()
        self.assertTrue(any(c.isupper() for c in password))
        self.assertTrue(any(c.isdigit() for c in password))

class TestSavePasswordHash(unittest.TestCase):
    """
    Tests unitaires pour la fonction save_password_hash().
    """

    def setUp(self):
        """
        Supprime le fichier de test avant chaque test.
        """
        if os.path.exists("passwords.json"):
            os.remove("passwords.json")

    def test_save_password_hash(self):
        """
        Teste que la fonction save_password_hash() sauvegarde correctement le hachage d'un mot de passe pour
        un utilisateur donné dans un fichier JSON.
        """
        save_password_hash("alice", "password123")

        with open("passwords.json", "r") as f:
            data = json.load(f)

        self.assertEqual(data, {"alice": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8"})


if __name__ == '__main__':
    unittest.main()
