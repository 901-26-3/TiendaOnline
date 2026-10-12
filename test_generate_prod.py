import pytest
from generate_prod import (
    generar_productos,
    generar_clave,
    PRODUCTOS,
    MARCAS,
)


@pytest.fixture
def productos():
    return generar_productos(100, seed=42)


def test_cantidad_de_productos(productos):
    assert len(productos) == 100


def test_cada_producto_tiene_cuatro_campos(productos):
    for producto in productos:
        assert set(producto.keys()) == {"producto", "clave", "precio", "marca"}


def test_producto_pertenece_al_catalogo(productos):
    for p in productos:
        assert p["producto"] in PRODUCTOS


def test_marca_pertenece_al_catalogo(productos):
    for p in productos:
        assert p["marca"] in MARCAS


def test_clave_tiene_6_caracteres(productos):
    for p in productos:
        assert len(p["clave"]) == 6


def test_clave_solo_mayusculas_y_digitos(productos):
    for p in productos:
        assert p["clave"].isalnum()
        assert p["clave"] == p["clave"].upper()


def test_precio_en_rango(productos):
    for p in productos:
        assert 100 <= p["precio"] <= 20000


def test_precio_tiene_maximo_dos_decimales(productos):
    for p in productos:
        assert round(p["precio"], 2) == p["precio"]


def test_precio_es_numero(productos):
    for p in productos:
        assert isinstance(p["precio"], float)


def test_claves_son_unicas(productos):
    claves = [p["clave"] for p in productos]
    assert len(claves) == len(set(claves))


def test_generar_clave_longitud_personalizada():
    assert len(generar_clave(10)) == 10


def test_cero_productos_devuelve_lista_vacia():
    assert generar_productos(0) == []