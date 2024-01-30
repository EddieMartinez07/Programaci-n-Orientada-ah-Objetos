class Aerolinea:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vuelos = []

    def agregar_vuelo(self, vuelo):
        self.vuelos.append(vuelo)
        print(f"Vuelo {vuelo.numero_vuelo} agregado a {self.nombre}")

    def mostrar_vuelos(self):
        print(f"Vuelos de {self.nombre}:")
        for vuelo in self.vuelos:
            print(f"Vuelo {vuelo.numero_vuelo}: {vuelo.origen} - {vuelo.destino}")

class Vuelo:
    def __init__(self, numero_vuelo, origen, destino):
        self.numero_vuelo = numero_vuelo
        self.origen = origen
        self.destino = destino
        self.pasajeros = []

    def agregar_pasajero(self, pasajero):
        self.pasajeros.append(pasajero)
        print(f"Pasajero {pasajero.nombre} agregado al vuelo {self.numero_vuelo}")

    def mostrar_pasajeros(self):
        print(f"Pasajeros del vuelo {self.numero_vuelo}:")
        for pasajero in self.pasajeros:
            print(pasajero.nombre)

class Pasajero:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

# Crear instancias
aerolinea1 = Aerolinea("Aerolínea A")
vuelo1 = Vuelo(101, "Ciudad A", "Ciudad B")
pasajero1 = Pasajero("Juan", 25)
pasajero2 = Pasajero("María", 30)

# Agregar vuelo a aerolínea
aerolinea1.agregar_vuelo(vuelo1)

# Agregar pasajeros al vuelo
vuelo1.agregar_pasajero(pasajero1)
vuelo1.agregar_pasajero(pasajero2)

# Mostrar información
aerolinea1.mostrar_vuelos()
vuelo1.mostrar_pasajeros()