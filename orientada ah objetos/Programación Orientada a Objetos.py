class InformacionClimatica:
    def __init__(self):
        self.temperaturas_diarias = []

    def ingresar_temperaturas_diarias(self):
        for dia in range(1, 8):
            temperatura = float(input(f"Ingrese la temperatura del día {dia}: "))
            self.temperaturas_diarias.append(temperatura)

    def calcular_promedio_semanal(self):
        if not self.temperaturas_diarias:
            print("Primero ingrese las temperaturas diarias.")
            return None
        else:
            promedio_semanal = sum(self.temperaturas_diarias) / len(self.temperaturas_diarias)
            return promedio_semanal

# Ejemplo de herencia, si se desea extender la clase en el futuro
class InformacionExtendida(InformacionClimatica):
    def __init__(self):
        super().__init__()
        self.otro_dato = None

    def ingresar_otro_dato(self):
        self.otro_dato = input("Ingrese otro dato relacionado con el clima: ")

    # Puedes agregar más métodos específicos para esta clase si es necesario

def main():
    # Ejemplo de uso de la clase base
    informacion_climatica = InformacionClimatica()
    informacion_climatica.ingresar_temperaturas_diarias()
    promedio_semanal = informacion_climatica.calcular_promedio_semanal()

    if promedio_semanal is not None:
        print("\nTemperaturas diarias ingresadas:", informacion_climatica.temperaturas_diarias)
        print("El promedio semanal es:", promedio_semanal)

    # Ejemplo de uso de la clase extendida
    informacion_extendida = InformacionExtendida()
    informacion_extendida.ingresar_temperaturas_diarias()
    informacion_extendida.ingresar_otro_dato()
    promedio_semanal_extendido = informacion_extendida.calcular_promedio_semanal()

    if promedio_semanal_extendido is not None:
        print("\nTemperaturas diarias ingresadas:", informacion_extendida.temperaturas_diarias)
        print("El promedio semanal es:", promedio_semanal_extendido)
        print("Otro dato relacionado con el clima:", informacion_extendida.otro_dato)

if __name__ == "__main__":
    main()
