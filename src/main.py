import hashlib
import string
import random
import json

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


def save_password_hash(username: str, password: str) -> None:
    """
    Sauvegarde le hachage SHA256 d'un mot de passe pour un utilisateur donné dans un fichier JSON.

    :param username: le nom d'utilisateur
    :param password: le mot de passe à hasher
    """
    # Hash le mot de passe avec SHA256
    password_hash = hashlib.sha256(password.encode("utf-8")).hexdigest()

    # Crée un dictionnaire avec le nom d'utilisateur et le hachage du mot de passe
    data = {username: password_hash}

    # Écrit le dictionnaire dans un fichier JSON
    with open("passwords.json", "w") as f:
        json.dump(data, f)
