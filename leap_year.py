def es_bisiesto(ano):
    """Función para determinar si un año dado es bisiesto."""
    return ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)

# Ejemplo de uso
ano = int(input("Ingrese un año: "))
if es_bisiesto(ano):
    print(f"{ano} es un año bisiesto.")
else:
    print(f"{ano} no es un año bisiesto.")
