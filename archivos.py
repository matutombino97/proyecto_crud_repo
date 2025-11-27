import csv

def convertir_csv_dict():
    productos = []
    with open('proyecto_Crud/data/productos.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for fila in reader:
            productos.append(fila)
    return productos


def guardar_csv(productos: list):
    with open('proyecto_Crud/data/productos.csv', 'w', newline='', encoding='utf-8') as file:
        fieldnames = ['id', 'nombre', 'precio', 'stock', 'categoria']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        for prod in productos:
            row = {clave: str(prod[clave]) for clave in fieldnames}
            writer.writerow(row)

    print("Cambios guardados en 'data/productos.csv'.")

