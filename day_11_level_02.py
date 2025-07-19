# 1. Contar números pares e impares hasta un número dado
def evens_and_odds(n):
    pares = 0
    impares = 0
    for i in range(n + 1):
        if i % 2 == 0:
            pares += 1
        else:
            impares += 1
    return f"El número de impares es {impares}.\nEl número de pares es {pares}."

print("#1:\n", evens_and_odds(100))
# El número de impares es 50.
# El número de pares es 51.

# 2. Calcular el factorial de un número
def factorial(n):
    if n < 0:
        return "No se puede calcular el factorial de un número negativo."
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

print("#2:", factorial(5))  # 120
print("#2:", factorial(0))  # 1

# 3. Comprobar si un valor está vacío
def is_empty(valor):
    return not bool(valor)

print("#3:", is_empty(""))     # True
print("#3:", is_empty([]))     # True
print("#3:", is_empty(0))      # True (porque 0 es falsy)
print("#3:", is_empty("Hola")) # False

# 4. Calcular media
def calculate_mean(lista):
    if not lista:
        return "Lista vacía"
    return sum(lista) / len(lista)

print("#4:", calculate_mean([1, 2, 3, 4, 5]))  # 3.0

# 5. Calcular mediana
def calculate_median(lista):
    if not lista:
        return "Lista vacía"
    lista_ordenada = sorted(lista)
    n = len(lista_ordenada)
    mitad = n // 2
    if n % 2 == 0:
        return (lista_ordenada[mitad - 1] + lista_ordenada[mitad]) / 2
    else:
        return lista_ordenada[mitad]

print("#5:", calculate_median([1, 2, 3, 4, 5]))       # 3
print("#5:", calculate_median([1, 2, 3, 4, 5, 6]))    # 3.5

# 6. Calcular moda
def calculate_mode(lista):
    if not lista:
        return "Lista vacía"
    from collections import Counter
    conteo = Counter(lista)
    max_frecuencia = max(conteo.values())
    moda = [k for k, v in conteo.items() if v == max_frecuencia]
    if len(moda) == len(lista):
        return "No hay moda"
    return moda

print("#6:", calculate_mode([1, 2, 3, 3, 4, 5]))  # [3]
print("#6:", calculate_mode([1, 2, 3, 4, 5]))     # No hay moda

# 7. Calcular rango
def calculate_range(lista):
    if not lista:
        return "Lista vacía"
    return max(lista) - min(lista)

print("#7:", calculate_range([1, 2, 3, 4, 5]))  # 4

# 8. Calcular varianza
def calculate_variance(lista):
    if not lista:
        return "Lista vacía"
    media = calculate_mean(lista)
    return sum((x - media) ** 2 for x in lista) / len(lista)

print("#8:", calculate_variance([1, 2, 3, 4, 5]))  # 2.0

# 9. Calcular desviación estándar
def calculate_std(lista):
    import math
    varianza = calculate_variance(lista)
    if isinstance(varianza, str):
        return varianza
    return math.sqrt(varianza)

print("#9:", calculate_std([1, 2, 3, 4, 5]))  # 1.41 aprox
