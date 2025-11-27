# Ajuste para documentación y preparación del README
from archivos import convertir_csv_dict, guardar_csv
from crud import agregar_prods, editar_prods, eliminar_prods, mostrar_producto
from utils import pausar, generar_id
from helpers import validar_texto, validar_numero
from consultas import filtrar_por_precio, sin_stock, filtrar_prod_por_categoria, buscar_por_nombre, buscar_por_rango, stock_critico, cantidad_por_categoria, precio_promedio, stock_total, producto_mas_caro_barato
from reportes.reportes import exportar_reportes_csv, exportar_reportes_json, exportar_reportes_txt
import sys

# Cada archivo cumple un rol:

# main.py → menú y flujo

# crud.py → crear/editar/eliminar/listar

# archivos.py → leer y guardar CSV

# utils.py → validaciones y funciones auxiliares
if __name__ == '__main__':

    productos = convertir_csv_dict()
    print('Total de productos cargados:', len(productos))

    menu = """
    ==============================
    MENÚ DE OPCIONES
    ==============================
    1. Listar productos
    2. Filtrar productos por precio
    3. Productos sin stock
    4. Filtrar por categoría
    5. Crear producto nuevo
    6. Editar producto
    7. Eliminar producto
    8. Buscar por nombre
    9. Buscar por rango de precios
    10. Stock crítico (<5)
    11. Reportes automaticos
    12. Exportar reportes (CSV)
    13. Exportar reportes (JSON)
    14. Exportar reportes (TXT)
    0. Salir
    ==============================
    """

    while True:
        print(menu)

        opcion = input("Ingrese una opción: ").strip()

        if not opcion.isdigit():
            print("Ingrese un número válido.")
            continue

        opcion = int(opcion)

        # ---------------------------------------------------
        # 1. Listar productos
        # ---------------------------------------------------
        if opcion == 1:
            try:
                for prod in productos:
                    mostrar_producto(prod)
            except Exception as e:
                print("Ocurrió un error inesperado:", e)

            pausar()

        # ---------------------------------------------------
        # 2. Filtrar por precio
        # ---------------------------------------------------
        elif opcion == 2:
            try:
                precio = input("Ingrese precio mínimo: ").strip()

                if precio.isdigit():
                    precio = int(precio)
                    filtrados = filtrar_por_precio(productos, precio)
                    print(f"Productos con precio mayor a {precio}: {len(filtrados)}")

                    for prod in filtrados:
                        mostrar_producto(prod)
                else:
                    print("Debe ingresar un número entero.")

            except Exception as e:
                print("Ocurrió un error inesperado:", e)

            pausar()

        # ---------------------------------------------------
        # 3. Productos sin stock
        # ---------------------------------------------------
        elif opcion == 3:
            try:
                sin = sin_stock(productos)
                print(f"Productos sin stock: {len(sin)}")

                for prod in sin:
                    mostrar_producto(prod)

            except Exception as e:
                print("Ocurrió un error inesperado:", e)

            pausar()

        # ---------------------------------------------------
        # 4. Filtrar por categoría
        # ---------------------------------------------------
        elif opcion == 4:
            try:
                categoria = input("Ingrese categoría: ").strip().lower()
                filtrados = filtrar_prod_por_categoria(productos, categoria)

                if filtrados:
                    print(f"Productos en categoría '{categoria}': {len(filtrados)}")
                    for prod in filtrados:
                        mostrar_producto(prod)
                else:
                    print("No se encontraron productos en esa categoría.")

            except Exception as e:
                print("Ocurrió un error inesperado:", e)

            pausar()

        # ---------------------------------------------------
        # 5. Crear producto nuevo
        # ---------------------------------------------------
        elif opcion == 5:
            try:
                agregar_prods(productos)
                print("✔ Producto agregado correctamente.")
            except Exception as e:
                print("Ocurrió un error inesperado:", e)

            pausar()

        # ---------------------------------------------------
        # 6. Editar producto
        # ---------------------------------------------------
        elif opcion == 6:
            try:
                editar_prods(productos)
                print("✔ Producto editado correctamente.")
            except Exception as e:
                print("Ocurrió un error inesperado:", e)

            pausar()

        # ---------------------------------------------------
        # 7. Eliminar producto
        # ---------------------------------------------------
        elif opcion == 7:
            try:
                eliminar_prods(productos)
                print("✔ Producto eliminado correctamente.")
            except Exception as e:
                print("Ocurrió un error inesperado:", e)

            pausar()

        elif opcion == 8:
            try:
                nombre = input("Ingrese parte del nombre a buscar: ").strip()
                encontrados = buscar_por_nombre(productos, nombre)

                print(f"Productos encontrados: {len(encontrados)}")
                for prod in encontrados:
                    mostrar_producto(prod)

            except Exception as e:
                print("Ocurrió un error inesperado:", e)

            pausar()

        elif opcion == 9:
            try:
                minimo = int(input("Precio mínimo: ").strip())
                maximo = int(input("Precio máximo: ").strip())

                encontrados = buscar_por_rango(productos, minimo, maximo)

                print(f"Productos entre ${minimo} y ${maximo}: {len(encontrados)}")
                for prod in encontrados:
                    mostrar_producto(prod)

            except ValueError:
                print("Debe ingresar valores numéricos.")
            except Exception as e:
                print("Ocurrió un error inesperado:", e)

            pausar()

        elif opcion == 10:
            try:
                criticos = stock_critico(productos)
                print(f"Productos con stock menor a 5: {len(criticos)}")

                for prod in criticos:
                    mostrar_producto(prod)

            except Exception as e:
                print("Ocurrió un error inesperado:", e)

            pausar()

        elif opcion == 11:
            try:
                print("----- Reportes Automáticos -----")
                print(f"Cantidad de productos por categoría: {cantidad_por_categoria(productos)}")
                print(f"Precio promedio de productos: ${precio_promedio(productos):.2f}")
                print(f"Stock total de productos: {stock_total(productos)} unidades")

                caro, barato = producto_mas_caro_barato(productos)
                if caro is None or barato is None:
                    print("No hay productos cargados para generar reportes.")
                else:
                    print("Producto más caro:")
                    mostrar_producto(caro)
                    print("Producto más barato:")
                    mostrar_producto(barato)

                print("Producto más caro:")
                mostrar_producto(caro)
                print("Producto más barato:")
                mostrar_producto(barato)

            except Exception as e:
                print("Ocurrió un error inesperado:", e)

            pausar()

        elif opcion == 12:
            ruta = "proyecto_Crud/reportes/productos_reportes.csv"
            
            if exportar_reportes_csv(productos, ruta):
                print(f"✔ Reporte CSV exportado en: {ruta}")
            else:
                print("❌ Error al exportar el CSV.")

            pausar()

        elif opcion == 13:
            ruta = "proyecto_Crud/reportes/productos_reportes.json"
            
            if exportar_reportes_json(productos, ruta):
                print(f"✔ Reporte JSON exportado en: {ruta}")
            else:
                print("❌ Error al exportar el JSON.")

            pausar()

        elif opcion == 14:
            if not productos:
                print("❌ No hay productos cargados para generar el reporte.")
                pausar()
                continue

            ruta = "proyecto_Crud/reportes/productos_reportes.txt"

            if exportar_reportes_txt(productos, ruta):
                print(f"✔ Reporte TXT creado en: {ruta}")
            else:
                print("❌ Error al exportar el TXT.")

            pausar()


        # ---------------------------------------------------
        # 0. Salir (con confirmación)
        # ---------------------------------------------------
        elif opcion == 0:

            while True:
                confirm = input("¿Desea guardar los cambios antes de salir? (s/n): ").strip().lower()

                if confirm == "s":
                    guardar_csv(productos)
                    print("Cambios guardados. ¡Hasta luego!")
                    sys.exit()

                elif confirm == "n":
                    print("Saliendo sin guardar cambios. ¡Hasta luego!")
                    sys.exit()

                else:
                    print("Opción inválida. Responda con 's' o 'n'.")

        else:
            print("Opción inválida, intente nuevamente.")
