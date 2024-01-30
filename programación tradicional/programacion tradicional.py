def obtener_temperaturas_diarias():
    temperaturas_diarias = []
    for dia in range(1, 8):
        temperatura = float(input(f"Ingrese la temperatura del día {dia}: "))
        temperaturas_diarias.append(temperatura)
    return temperaturas_diarias

def calcular_promedio_semanal(temperaturas_diarias):
    promedio_semanal = sum(temperaturas_diarias) / len(temperaturas_diarias)
    return promedio_semanal

def main():
    temperaturas_diarias = obtener_temperaturas_diarias()
    promedio_semanal = calcular_promedio_semanal(temperaturas_diarias)

    print("\nTemperaturas diarias ingresadas:", temperaturas_diarias)
    print("El promedio semanal es:", promedio_semanal)

if __name__ == "__main__":
    main()
