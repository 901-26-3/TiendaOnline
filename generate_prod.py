import random
import secrets
import string

PRODUCTOS = [
    "Laptop", "Mouse", "Teclado", "Monitor", "Impresora",
    "Audifonos", "Tablet", "Webcam", "Bocinas", "Microfono",
    "Memoria USB", "Disco Duro", "Cargador", "Router", "Camara"
]

MARCAS = [
    "HP", "Dell", "Lenovo", "Logitech", "Samsung",
    "Apple", "Asus", "Acer", "Sony", "Microsoft"
]

CARACTERES = string.ascii_uppercase + string.digits


def generar_clave(longitud=6):
    return ''.join(secrets.choice(CARACTERES) for _ in range(longitud))


def generar_productos(num_productos, seed=None):
    if seed is not None:
        random.seed(seed)

    productos = []

    for i in range(num_productos):
        producto = random.choice(PRODUCTOS)
        clave = generar_clave()
        precio = round(random.uniform(100, 20000), 2)
        marca = random.choice(MARCAS)

        productos.append({
            "producto": producto,
            "clave": clave,
            "precio": precio,
            "marca": marca
        })

    return productos


if __name__ == "__main__":
    for producto in generar_productos(100):
        print(producto)