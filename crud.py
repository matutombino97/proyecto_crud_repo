from utils import generar_id, pausar    
from helpers import validar_texto, validar_numero   
from archivos import guardar_csv

def mostrar_producto(producto): 
    print("Producto: #",producto['id']) 
    print("Nombre:", producto['nombre']) 
    print("Precio: $",producto['precio']) 
    print("Stock:", producto["stock"]) 
    print("Categoria:", producto['categoria']) 
    print("-" * 40)

def agregar_prods(productos: list) -> list:
    try:
        nombre = validar_texto(input("Ingrese nombre: "), "nombre")
        precio = validar_numero(input("Ingrese precio: "), "precio")
        stock = validar_numero(input("Ingrese stock: "), "stock")
        categoria = validar_texto(input("Ingrese categoría: "), "categoría").lower()

        nuevo_producto = {
            "id": generar_id(productos),
            "nombre": nombre,
            "precio": precio,
            "stock": stock,
            "categoria": categoria
        }

        productos.append(nuevo_producto)
        print("Producto agregado:", nuevo_producto)
        guardar_csv(productos)

    except ValueError as e:
        print("Error:", e)

    return productos


def editar_prods(productos: list):
    try:
        id_buscar = input("Ingrese el ID a buscar: ").strip()

        if not id_buscar.isdigit():
            raise ValueError("Debe ingresar un número válido.")

        id_buscar = int(id_buscar)

        for prod in productos:
            if int(prod['id']) == id_buscar:
                print("Producto encontrado:")
                print(prod)

                print("""
                ¿Qué desea editar?
                1. Nombre
                2. Precio
                3. Stock
                4. Categoría
                0. Cancelar
                """)

                opcion = input("Ingrese la opción deseada: ").strip()

                if opcion == "1":
                    prod['nombre'] = validar_texto(input("Nuevo nombre: "), "nombre")

                elif opcion == "2":
                    prod['precio'] = validar_numero(input("Ingrese el precio nuevo: "), "precio")

                elif opcion == "3":
                    prod['stock'] = validar_numero(input("Ingrese el stock nuevo: "), "stock")

                elif opcion == "4":
                    prod['categoria'] = validar_texto(input("Ingrese la categoría nueva: "), "categoría").lower()

                elif opcion == "0":
                    print("Edición cancelada.")
                    return productos

                else:
                    print("Opción inválida.")
                    return productos

                print("Producto actualizado correctamente:", prod)
                guardar_csv(productos)
                return productos

        print("No se encontró un producto con ese ID.")

    except ValueError as e:
        print("Error:", e)

    return productos


def eliminar_prods(productos: list):
    id_buscar = input("Ingrese el ID del producto a eliminar: ").strip()

    if not id_buscar.isdigit():
        print("Debe ingresar un número válido.")
        return productos

    id_buscar = int(id_buscar)

    for prod in productos:
        if int(prod['id']) == id_buscar:
            print("Producto encontrado:", prod)

            opcion = input("¿Está seguro que desea eliminar este producto? (s/n): ").strip().lower()

            if opcion != 's':
                print("Eliminación cancelada.")
                return productos

            productos.remove(prod)
            print("Producto eliminado:", prod)

            guardar_csv(productos)
            return productos

    print("No se encontró un producto con ese ID.")
    return productos
