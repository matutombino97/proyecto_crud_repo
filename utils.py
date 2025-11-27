def generar_id(productos: list) -> int:
    if not productos:
        return 1
    return max(int(p["id"]) for p in productos) + 1


def pausar():
    input("Presione Enter para continuar...")

