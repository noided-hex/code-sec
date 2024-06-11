import hashlib
import string
import random

def add(a, b):
    return a + b

def sha256(message: str) -> str:
    """
    Produit une empreinte SHA256 à partir d'une chaîne de caractères.

    :param message: la chaîne de caractères à hasher
    :return: l'empreinte SHA256 sous forme de chaîne de caractères hexadécimale
    """
    # Encode la chaîne de caractères en bytes
    message_bytes = message.encode("utf-8")

    # Crée un objet hashlib.sha256 et met à jour l'empreinte avec les bytes de la chaîne de caractères
    sha256_hash = hashlib.sha256(message_bytes)

    # Retourne l'empreinte sous forme de chaîne de caractères hexadécimale
    return sha256_hash.hexdigest()


def generate_password():
    """
    Génère un mot de passe aléatoire entre 8 et 12 caractères.
    """
    length = random.randint(8, 12)
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))
    return password

password1 = generate_password()
print(password1)
