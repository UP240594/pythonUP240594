'''Ejercicios dia 1'''
#Tipos de datos en python
print(1500)          # Int
print(3.14)        # Float
print(15 + 8j)      # Complex number
print('Amo programar')  # String
print(True)    # Boolean
print([1, 2, 3, 4, 5])   # List
print((9.8, 7.5, 8.9))    # Tuple
print({9.8, 7.5, 8.9})    # Set
print({'color':'amarillo'}) # Dictionary

#Distancia euclidiana

# Coordenadas de los puntos
x1 = 2
y1 = 3

x2 = 10
y2 = 8

# Resta de coordenadas
dx = x2 - x1  # 10 - 2 = 8
dy = y2 - y1  # 8 - 3 = 5

# Elevar al cuadrado las diferencias
dx_cuadrada = dx * dx     # 8 * 8 = 64
dy_cuadrada = dy * dy     # 5 * 5 = 25

#suma de c
suma = dx_cuadrada + dy_cuadrada # 64 + 25 = 89

#raiz cuadrada
distancia = suma ** 0.5


print("La distancia inclinada es:", distancia)