import os

MAX_NOMBRE = 20
MAX_INVENTARIO = 13

class Ropa:
    def __init__(self, nombre="", cantidad=0, precio=0.0):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

def guardar_inventario_en_archivo(inventario):
    with open("inventario.txt", "w") as archivo:
        for ropa in inventario:
            if ropa.nombre:
                archivo.write(f"{ropa.nombre} {ropa.cantidad} {ropa.precio:.2f}\n")

def cargar_inventario_desde_archivo(inventario):
    if not os.path.exists("inventario.txt"):
        print("No se encontró el archivo de inventario.")
        return

    with open("inventario.txt", "r") as archivo:
        for i, linea in enumerate(archivo):
            if i >= MAX_INVENTARIO:
                break
            nombre, cantidad, precio = linea.strip().split()
            inventario[i] = Ropa(nombre, int(cantidad), float(precio))

def ingresar_nueva_ropa(inventario):
    ropa_ingresada = input("¿Qué tipo de ropa quieres ingresar?\n")
    unidad_ropa = int(input(f"¿Cuántas unidades de {ropa_ingresada} quieres ingresar?\n"))
    precio_ropa = float(input(f"¿Cuál es el precio de {ropa_ingresada}?\n"))

    indice_ropa = buscar_por_nombre(inventario, ropa_ingresada)

    if indice_ropa != -1:
        inventario[indice_ropa].precio = precio_ropa
        inventario[indice_ropa].cantidad += unidad_ropa
        print(f"Se han agregado {unidad_ropa} unidades de {ropa_ingresada} al inventario.")
    else:
        for ropa in inventario:
            if not ropa.nombre:
                ropa.nombre = ropa_ingresada
                ropa.cantidad = unidad_ropa
                ropa.precio = precio_ropa
                print(f"Se han agregado {unidad_ropa} unidades de {ropa_ingresada} al inventario.")
                break

    guardar_inventario_en_archivo(inventario)

def editar_prenda(inventario):
    nombre_a_buscar = input("Ingrese el nombre de la prenda que desea editar: ")
    indice = buscar_por_nombre(inventario, nombre_a_buscar)

    if indice != -1:
        nuevo_valor = int(input("Ingrese la nueva cantidad: "))
        nuevo_precio = float(input("Ingrese el nuevo precio: "))
        inventario[indice].cantidad = nuevo_valor
        inventario[indice].precio = nuevo_precio
        print("Prenda actualizada exitosamente.")
    else:
        print("El nombre buscado no existe.")

    guardar_inventario_en_archivo(inventario)

def eliminar_prenda(inventario):
    nombre_a_buscar = input("Ingrese el nombre de la prenda que desea eliminar: ")
    indice = buscar_por_nombre(inventario, nombre_a_buscar)

    if indice != -1:
        inventario[ind
