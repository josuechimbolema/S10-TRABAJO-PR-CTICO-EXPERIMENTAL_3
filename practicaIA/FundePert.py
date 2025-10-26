def triangular(x, a, b, c):
    """
    Función de pertenencia triangular.
    a: inicio de la base
    b: punto máximo (grado 1)
    c: fin de la base
    """
    if x <= a or x >= c:
        return 0
    elif a < x <= b:
        return (x - a) / (b - a)
    elif b < x < c:
        return (c - x) / (c - b)
    else:
        return 0


# Ejemplo: temperatura "cálida" en el rango [15, 25, 35]
temperatura = 25
grado = triangular(temperatura, 15, 25, 35)

# Mostrar el resultado formateado
print(f"Grado de pertenencia de {temperatura}°C a 'cálida': {grado:.2f}")
