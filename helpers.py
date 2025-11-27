def validar_numero(numero: str, campo: str):
    numero = numero.strip()
    if not numero.isdigit():
        raise ValueError(f"El campo '{campo}' debe ser un número entero.")
    numero = int(numero)
    if numero < 0:
        raise ValueError(f"El campo '{campo}' no puede ser negativo.")
    return numero

def validar_texto(texto: str, campo: str):
    texto = texto.strip()
    if texto:
        return texto
    else:
        raise ValueError(f"El campo '{campo}' no puede estar vacío.")
