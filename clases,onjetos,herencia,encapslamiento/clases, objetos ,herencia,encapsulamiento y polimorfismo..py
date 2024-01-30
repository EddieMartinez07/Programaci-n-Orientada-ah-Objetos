class Animal:
    def __init__(self, nombre):
        self._nombre = nombre  # Encapsulación utilizando un guion bajo al inicio

    def hacer_sonido(self):
        pass  # Método que será sobrescrito por las clases derivadas


class Perro(Animal):
    def hacer_sonido(self):
        return "Guau"  # Sobrescribiendo el método de la clase base


# Creando instancias de las clases
animal_generico = Animal("Criatura")
perro = Perro("Buddy")

# Demostrando polimorfismo al llamar al método hacer_sonido en ambas instancias
print(f"{animal_generico._nombre} hace un sonido: {animal_generico.hacer_sonido()}")
print(f"{perro._nombre} hace un sonido: {perro.hacer_sonido()}")
