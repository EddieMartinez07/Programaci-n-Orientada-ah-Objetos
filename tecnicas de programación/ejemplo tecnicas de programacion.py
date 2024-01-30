class Empleado:

    def __init__(self, nombre, salario_base):
        self.nombre = nombre
        self.__salario_base = salario_base  # Encapsulación

    def calcular_salario(self):
        return self.__salario_base

    def mostrar_informacion(self):
        print("Empleado:", self.nombre)
        print("Salario Base:", self.__salario_base)


class Gerente(Empleado):

    def __init__(self, nombre, salario_base, bono):
        super().__init__(nombre, salario_base)
        self.__bono = bono  # Encapsulación

    def calcular_salario(self):  # Polimorfismo
        return super().calcular_salario() + self.__bono

    def mostrar_informacion(self):  # Polimorfismo
        super().mostrar_informacion()
        print("Bono:", self.__bono)


class Desarrollador(Empleado):

    def __init__(self, nombre, salario_base, lenguaje):
        super().__init__(nombre, salario_base)
        self.lenguaje = lenguaje  # Abstracción

    def mostrar_informacion(self):  # Polimorfismo
        super().mostrar_informacion()
        print("Lenguaje de Programación:", self.lenguaje)


# Uso de las clases
empleado_1 = Empleado("Juan", 50000)
gerente_1 = Gerente("Ana", 70000, 10000)
desarrollador_1 = Desarrollador("Carlos", 60000, "Python")

# Mostrar información y salario de cada empleado
print("Información del Empleado:")
empleado_1.mostrar_informacion()
print("Salario:", empleado_1.calcular_salario())

print("\nInformación del Gerente:")
gerente_1.mostrar_informacion()
print("Salario:", gerente_1.calcular_salario())

print("\nInformación del Desarrollador:")
desarrollador_1.mostrar_informacion()
print("Salario:", desarrollador_1.calcular_salario())
