import json

class Inventario:
    def __init__(self):
        self.inventario = {}

    def cargar_inventario(self, archivo):
        try:
            with open(archivo, 'r') as f:
                self.inventario = json.load(f)
        except FileNotFoundError:
            print("El archivo de inventario no existe. Se creará uno nuevo.")
            self.guardar_inventario(archivo)
        except PermissionError:
            print("No tienes permisos para leer el archivo de inventario.")

    def guardar_inventario(self, archivo):
        try:
            with open(archivo, 'w') as f:
                json.dump(self.inventario, f, indent=4)
                print("Inventario guardado exitosamente.")
        except PermissionError:
            print("No tienes permisos para escribir en el archivo de inventario.")

    def agregar_producto(self, producto, cantidad):
        if producto in self.inventario:
            self.inventario[producto] += cantidad
        else:
            self.inventario[producto] = cantidad

    def actualizar_producto(self, producto, cantidad):
        self.inventario[producto] = cantidad

    def eliminar_producto(self, producto):
        del self.inventario[producto]


# Ejemplo de uso
archivo_inventario = 'inventario.txt'
inventario = Inventario()
inventario.cargar_inventario(archivo_inventario)

# Agregar productos al inventario
inventario.agregar_producto('Manzanas', 50)
inventario.agregar_producto('Plátanos', 30)

# Actualizar productos en el inventario
inventario.actualizar_producto('Manzanas', 60)

# Eliminar un producto del inventario
inventario.eliminar_producto('Plátanos')

# Guardar el inventario en el archivo
inventario.guardar_inventario(archivo_inventario)
