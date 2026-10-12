import pytest
from generate import generar_productos, PRODUCTOS, MARCAS


@pytest.fixture
def productos():
    return generar_productos(100, seed=42)


def test_cantidad_de_productos(productos):
    assert len(productos) == 100


def test_cada_producto_tiene_cuatro_campos(productos):
    for producto in productos:
        assert len(producto) == 4
        assert "producto" in producto
        assert "clave" in producto
        assert "precio" in producto
        assert "marca" in producto


def test_clave_tiene_seis_caracteres(productos):
    for producto in productos:
        assert len(producto["clave"]) == 6


def test_clave_contiene_solo_mayusculas_y_numeros(productos):
    caracteres_validos = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    for producto in productos:
        assert all(
            caracter in caracteres_validos
            for caracter in producto["clave"]
        )


def test_precios_son_validos(productos):
    for producto in productos:
        assert isinstance(producto["precio"], float)
        assert 100 <= producto["precio"] <= 20000


def test_nombres_de_productos_son_validos(productos):
    for producto in productos:
        assert producto["producto"] in PRODUCTOS


def test_marcas_son_validas(productos):
    for producto in productos:
        assert producto["marca"] in MARCAS


def test_claves_son_unicas(productos):
    claves = [producto["clave"] for producto in productos]
    assert len(claves) == len(set(claves))


def test_cantidad_negativa():
    assert generar_productos(-1) == []


def test_lista_vacia():
    assert generar_productos(0) == []