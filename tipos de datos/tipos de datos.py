# Programa: Calculadora de Área de Triángulo
# Descripción: Este programa calcula el área de un triángulo utilizando la fórmula A = (base * altura) / 2.

def calcular_area(base, altura):
    """
    Calcula el área de un triángulo.

    :param base: La base del triángulo.
    :param altura: La altura del triángulo.
    :return: El área del triángulo.
    """
    area = (base * altura) / 2
    return area

# Solicitar al usuario los valores de la base y la altura
base_triangulo = float(input("Ingrese la base del triángulo: "))
altura_triangulo = float(input("Ingrese la altura del triángulo: "))

# Calcular y mostrar el área del triángulo
area_resultante = calcular_area(base_triangulo, altura_triangulo)
print(f"El área del triángulo con base {base_triangulo} y altura {altura_triangulo} es: {area_resultante}")
