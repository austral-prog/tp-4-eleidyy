def calcular_y(coeficiente_A, coeficiente_B, coordenada_X):
    """Calcula la coordenada Y correspondiente a una coordenada X en la recta."""
    return coeficiente_A * coordenada_X + coeficiente_B

def calcular_distancia(x1, y1, x2, y2):
    """Calcula la distancia entre dos puntos en un plano."""
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

# Solicitar coeficientes y coordenadas X
coeficiente_A = float(input("Ingrese el coeficiente A: "))
coeficiente_B = float(input("Ingrese el coeficiente B: "))
coordenada_X1 = float(input("Ingrese el coeficiente X1: "))
coordenada_X2 = float(input("Ingrese el coeficiente X2: "))

# Calcular coordenadas Y
coordenada_Y1 = calcular_y(coeficiente_A, coeficiente_B, coordenada_X1)
coordenada_Y2 = calcular_y(coeficiente_A, coeficiente_B, coordenada_X2)

# Mostrar información de la ecuación
print(f"\nEl coeficiente A de su ecuación de la recta es: {coeficiente_A}")
print(f"El coeficiente B de su ecuación de la recta es: {coeficiente_B}")
print(f"El coeficiente X1 de su ecuación de la recta es: {coordenada_X1}")
print(f"El coeficiente X2 de su ecuación de la recta es: {coordenada_X2}")

print("\nPara la siguiente ecuación:")
print(f"\tY = {coeficiente_A}X + {coeficiente_B}\n")

# Mostrar información de los puntos
print("Dados los siguientes puntos:")
print(f"\tP1 ({coordenada_X1}, {coordenada_Y1})")
print(f"\tP2 ({coordenada_X2}, {coordenada_Y2})")

# Calcular y mostrar la distancia entre los puntos
distancia = calcular_distancia(coordenada_X1, coordenada_Y1, coordenada_X2, coordenada_Y2)
print(f"\nLa distancia entre ellos es: {distancia}")
