import pytest
from generate import generate_user_data, es_email_valido


@pytest.fixture
def usuarios():
    return generate_user_data(100, seed=42)


def test_cantidad_de_usuarios(usuarios):
    assert len(usuarios) == 100


def test_cada_usuario_tiene_tres_campos(usuarios):
    for usuario in usuarios:
        assert len(usuario) == 3


def test_password_tiene_12_caracteres(usuarios):
    for _, password, _ in usuarios:
        assert len(password) == 12


def test_emails_son_validos(usuarios):
    for _, _, email in usuarios:
        assert es_email_valido(email)


def test_usernames_son_unicos(usuarios):
    usernames = [u[0] for u in usuarios]
    assert len(usernames) == len(set(usernames))


def test_email_coincide_con_username(usuarios):
    for username, _, email in usuarios:
        assert email.startswith(username)


def test_email_invalido_es_rechazado():
    assert not es_email_valido("correo-sin-arroba.com")