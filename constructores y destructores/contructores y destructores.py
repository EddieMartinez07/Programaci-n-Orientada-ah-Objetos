class Persona:
    def __init__(self, nombre, edad):
        """
        Constructor de la clase Persona.

        Parameters:
        - nombre (str): El nombre de la persona.
        - edad (int): La edad de la persona.
        """
        self.nombre = nombre
        self.edad = edad
        print(f"Se ha creado una nueva persona: {self.nombre}, {self.edad} años.")

    def __del__(self):
        """
        Destructor de la clase Persona.
        Se ejecuta cuando el objeto es eliminado, por ejemplo, al finalizar el programa.
        """
        print(f"Se ha eliminado a la persona: {self.nombre}.")


# Crear instancias de la clase Persona
persona1 = Persona("Alice", 25)
persona2 = Persona("Bob", 30)

# Mostrar información de las personas
print(f"{persona1.nombre} tiene {persona1.edad} años.")
print(f"{persona2.nombre} tiene {persona2.edad} años.")

# El objeto persona2 será eliminado explícitamente usando del
del persona2
