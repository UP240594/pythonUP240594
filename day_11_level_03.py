# 1. Verificar si un número es primo
def is_prime(n):
    """Devuelve True si n es primo, False en caso contrario."""
    if not isinstance(n, int) or n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

print("#1:", is_prime(11))  # True
print("#1:", is_prime(12))  # False

# 2. Verificar que todos los ítems en una lista sean únicos
def all_unique(lista):
    """Devuelve True si todos los elementos en la lista son distintos."""
    return len(lista) == len(set(lista))

print("#2:", all_unique([1, 2, 3, 4]))   # True
print("#2:", all_unique([1, 2, 2, 3]))   # False

# 3. Verificar que todos los ítems sean del mismo tipo de dato
def all_same_type(lista):
    """Devuelve True si todos los elementos en la lista tienen el mismo tipo."""
    if not lista:
        return True
    tipo0 = type(lista[0])
    return all(isinstance(x, tipo0) for x in lista)

print("#3:", all_same_type([1, 2, 3]))     # True
print("#3:", all_same_type([1, '2', 3]))   # False

# 4. Verificar si una variable es un nombre válido en Python
import keyword
import re

def is_valid_python_variable(name):
    """
    Devuelve True si 'name' es un identificador válido en Python y no es palabra reservada.
    """
    if not isinstance(name, str):
        return False
    if keyword.iskeyword(name):
        return False
    return re.match(r'^[A-Za-z_][A-Za-z0-9_]*$', name) is not None

print("#4:", is_valid_python_variable("variable1"))  # True
print("#4:", is_valid_python_variable("1variable"))  # False
print("#4:", is_valid_python_variable("for"))        # False

# 5 y 6. Datos incluidos directamente en el archivo
countries = [
    {'name': 'China', 'languages': ['Chinese'], 'population': 1402112000},
    {'name': 'India', 'languages': ['Hindi', 'English'], 'population': 1359930000},
    {'name': 'United States', 'languages': ['English'], 'population': 329256000},
    {'name': 'Indonesia', 'languages': ['Indonesian'], 'population': 268074600},
    {'name': 'Brazil', 'languages': ['Portuguese'], 'population': 211715000},
    {'name': 'Pakistan', 'languages': ['Urdu', 'English'], 'population': 216565000},
    {'name': 'Nigeria', 'languages': ['English'], 'population': 200963000},
    {'name': 'Russia', 'languages': ['Russian'], 'population': 146793744},
    {'name': 'Bangladesh', 'languages': ['Bengali'], 'population': 168304408},
    {'name': 'Mexico', 'languages': ['Spanish'], 'population': 126190788},
    {'name': 'Germany', 'languages': ['German'], 'population': 83019200},
    {'name': 'France', 'languages': ['French'], 'population': 67060000},
    {'name': 'Spain', 'languages': ['Spanish'], 'population': 47329981},
    {'name': 'Canada', 'languages': ['English', 'French'], 'population': 38008005},
]

# 5. Idiomas más hablados en el mundo (por número de países donde se habla)
def most_spoken_languages(n=10):
    """
    Devuelve una lista de tuplas (idioma, cantidad_de_países) con los n idiomas más hablados,
    ordenados de mayor a menor según en cuántos países se habla.
    """
    from collections import Counter
    contador = Counter()
    for pais in countries:
        for idioma in pais.get('languages', []):
            contador[idioma] += 1
    return contador.most_common(n)

print("#5:", most_spoken_languages(10))

# 6. Países más poblados del mundo (top 10)
def most_populated_countries(n=10):
    """
    Devuelve una lista de tuplas (país, población) con los n países más poblados,
    ordenados de mayor a menor población.
    """
    ordenados = sorted(countries, key=lambda p: p.get('population', 0), reverse=True)
    return [(p['name'], p['population']) for p in ordenados[:n]]

print("#6:", most_populated_countries(10))
