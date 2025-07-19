
# 1. Filtrar solo números negativos y ceros
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negativos_y_ceros = [n for n in numbers if n <= 0]
print("#1:", negativos_y_ceros)  # [-4, -3, -2, -1, 0]

# 2. Aplanar lista de listas de listas a una sola lista
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
aplanada = [num for sublist in list_of_lists for inner in sublist for num in inner]
print("#2:", aplanada)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 3. Crear lista de tuplas con patrón matemático usando comprensión de listas
tuplas = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]
print("#3:")
for t in tuplas:
    print(t)

# 4. Aplanar lista de países a una nueva estructura en mayúsculas y abreviaturas
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flattened = [[pais.upper(), pais[:3].upper(), ciudad.upper()] 
             for pair in countries for (pais, ciudad) in pair]
print("#4:", flattened)

# 5. Convertir la lista anterior a diccionarios
dicts = [{'country': pais.upper(), 'city': ciudad.upper()}
         for pair in countries for (pais, ciudad) in pair]
print("#5:", dicts)

# 6. Convertir lista de nombres a lista de strings concatenados
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
full_names = [f"{nombre} {apellido}" 
              for pair in names for (nombre, apellido) in pair]
print("#6:", full_names)
# ['Asabeneh Yetayeh', 'David Smith', ...]

# 7. Lambda para calcular pendiente o intersección
# y = mx + b
# Pendiente (slope): (y2 - y1) / (x2 - x1)
# Intersección en y: y - m*x

slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1) if x2 != x1 else "Indefinida"
intercept = lambda x, y, m: y - m * x

print("#7:")
print("Pendiente:", slope(1, 2, 3, 6))     # 2.0
print("Intersección en y:", intercept(3, 6, 2))  # 0
