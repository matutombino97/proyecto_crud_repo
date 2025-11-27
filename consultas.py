def filtrar_por_precio(productos: list, precio_min: int):
    lista_filtrada = []
    for prod in productos:
        if int(prod['precio']) > precio_min:
            lista_filtrada.append(prod)
    return lista_filtrada


def sin_stock(productos: list):
    productos_sin_stock = []
    for dato in productos:
        if int(dato['stock']) == 0:
            productos_sin_stock.append(dato)
    return productos_sin_stock


def filtrar_prod_por_categoria(productos: list, categoria: str):
    nuevos_prod = []
    for prod in productos:
        if prod['categoria'].lower() == categoria.lower():
            nuevos_prod.append(prod)
    return nuevos_prod

def buscar_por_nombre(productos: list, texto: str):
    texto = texto.lower().strip()
    return [p for p in productos if texto in p["nombre"].lower()]


def buscar_por_rango(productos: list, minimo: int, maximo: int):
    lista = []
    for p in productos:
        precio = int(p["precio"])
        if minimo <= precio <= maximo:
            lista.append(p)
    return lista


def stock_critico(productos: list, limite: int = 5):
    return [p for p in productos if int(p["stock"]) < limite]


def cantidad_por_categoria(productos: list):
    categoria = {}
    for p in productos:
        cat = p["categoria"].lower()
        if cat in categoria:
            categoria[cat] += 1
        else:
            categoria[cat] = 1
    return categoria

def precio_promedio(productos: list) -> float:
    if not productos:
        return 0.0
    total = sum(int(p["precio"]) for p in productos)
    return total / len(productos)

def stock_total(productos: list) -> int:
    return sum(int(p["stock"]) for p in productos)

def producto_mas_caro_barato(productos: list):
    if not productos:
        return None, None

    mas_caro = max(productos, key=lambda p: int(p["precio"]))
    mas_barato = min(productos, key=lambda p: int(p["precio"]))

    return mas_caro, mas_barato 



