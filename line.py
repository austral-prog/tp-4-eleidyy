# Solicitar coeficientes y coordenadas X
coeficiente_A = float(input("Ingrese el coeficiente A: "))
coeficiente_B = float(input("Ingrese el coeficiente B: "))
coordenada_X1 = float(input("Ingrese el coeficiente X1: "))
coordenada_X2 = float(input("Ingrese el coeficiente X2: "))

# Calcular las coordenadas Y correspondientes
coordenada_Y1 = coeficiente_A * coordenada_X1 + coeficiente_B
coordenada_Y2 = coeficiente_A * coordenada_X2 + coeficiente_B

# Calcular la distancia entre los puntos
distancia = abs(coordenada_Y2 - coordenada_Y1)

# Mostrar resultados
print(f"\nPara la ecuación Y = {coeficiente_A}X + {coeficiente_B}:")
print(f"\tP1 ({coordenada_X1}, {coordenada_Y1})")
print(f"\tP2 ({coordenada_X2}, {coordenada_Y2})")

print(f"\nLa distancia entre los puntos es: {distancia}")
