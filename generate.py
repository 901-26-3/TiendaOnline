import random
import secrets

NOMBRES = ["carlos", "maria", "juan", "ana", "luis", "sofia", "pedro", "lucia"]
APELLIDOS = ["garcia", "lopez", "martinez", "hernandez", "perez", "ramirez"]
CARACTERES = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"


def generate_user_data(num_users, seed=None):
    if seed is not None:
        random.seed(seed)

    users = []
    for i in range(num_users):
        username = f"{random.choice(NOMBRES)}.{random.choice(APELLIDOS)}{i}"
        password = ''.join(secrets.choice(CARACTERES) for _ in range(12))
        email = f"{username}@example.com"
        users.append((username, password, email))
    return users


def es_email_valido(email):
    return "@" in email and email.endswith(".com")


if __name__ == "__main__":
    for user in generate_user_data(100):
        print(user)