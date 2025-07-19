# 1. Declarar una función que suma dos números
def add_two_numbers(a, b):
    return a + b

print("#1:", add_two_numbers(3, 4))  # 7

# 2. Calcular el área de un círculo
import math

def area_of_circle(radio):
    return math.pi * radio * radio

print("#2:", area_of_circle(5))  # 78.54 aprox

# 3. Sumar todos los argumentos (verificando que sean números)
def add_all_nums(*args):
    suma = 0
    for arg in args:
        if not isinstance(arg, (int, float)):
            return "Todos los elementos deben ser números."
        suma += arg
    return suma

print("#3:", add_all_nums(1, 2, 3, 4))  # 10
print("#3:", add_all_nums(1, 'a', 3))  # Error

# 4. Convertir °C a °F
def convert_celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

print("#4:", convert_celsius_to_fahrenheit(0))    # 32.0
print("#4:", convert_celsius_to_fahrenheit(100))  # 212.0

# 5. Determinar la estación del año según el mes
def check_season(mes):
    mes = mes.lower()
    if mes in ['diciembre', 'enero', 'febrero']:
        return 'Invierno'
    elif mes in ['marzo', 'abril', 'mayo']:
        return 'Primavera'
    elif mes in ['junio', 'julio', 'agosto']:
        return 'Verano'
    elif mes in ['septiembre', 'octubre', 'noviembre']:
        return 'Otoño'
    else:
        return 'Mes inválido'

print("#5:", check_season('Enero'))  # Invierno

# 6. Calcular la pendiente de una ecuación lineal
def calculate_slope(x1, y1, x2, y2):
    if x2 - x1 == 0:
        return "Pendiente indefinida"
    return (y2 - y1) / (x2 - x1)

print("#6:", calculate_slope(1, 2, 3, 6))  # 2.0

# 7. Resolver una ecuación cuadrática
def solve_quadratic_eqn(a, b, c):
    discriminante = b**2 - 4*a*c
    if discriminante < 0:
        return "No hay soluciones reales"
    elif discriminante == 0:
        x = -b / (2*a)
        return (x,)
    else:
        x1 = (-b + math.sqrt(discriminante)) / (2*a)
        x2 = (-b - math.sqrt(discriminante)) / (2*a)
        return (x1, x2)

print("#7:", solve_quadratic_eqn(1, -3, 2))  # (2.0, 1.0)

# 8. Imprimir elementos de una lista
def print_list(lista):
    for item in lista:
        print(item)

print("#8:")
print_list(['a', 'b', 'c'])

# 9. Invertir una lista usando bucles
def reverse_list(arr):
    reversed_arr = []
    for i in range(len(arr)-1, -1, -1):
        reversed_arr.append(arr[i])
    return reversed_arr

print("#9:", reverse_list([1, 2, 3, 4, 5]))  # [5, 4, 3, 2, 1]
print("#9:", reverse_list(["A", "B", "C"]))  # ["C", "B", "A"]

# 10. Capitalizar elementos de una lista
def capitalize_list_items(lista):
    return [item.capitalize() for item in lista]

print("#10:", capitalize_list_items(['tomato', 'potato', 'apple']))  # ['Tomato', 'Potato', 'Apple']

# 11. Agregar un ítem a una lista
def add_item(lista, item):
    return lista + [item]

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print("#11:", add_item(food_staff, 'Meat'))  # ['Potato', 'Tomato', 'Mango', 'Milk', 'Meat']
numbers = [2, 3, 7, 9]
print("#11:", add_item(numbers, 5))  # [2, 3, 7, 9, 5]

# 12. Eliminar un ítem de una lista
def remove_item(lista, item):
    return [i for i in lista if i != item]

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print("#12:", remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk']
numbers = [2, 3, 7, 9]
print("#12:", remove_item(numbers, 3))  # [2, 7, 9]

# 13. Suma de números del 1 al n
def sum_of_numbers(n):
    return sum(range(n + 1))

print("#13:", sum_of_numbers(5))    # 15
print("#13:", sum_of_numbers(10))   # 55
print("#13:", sum_of_numbers(100))  # 5050

# 14. Suma de impares en un rango
def sum_of_odds(n):
    return sum(i for i in range(n + 1) if i % 2 != 0)

print("#14:", sum_of_odds(10))  # 25

# 15. Suma de pares en un rango
def sum_of_even(n):
    return sum(i for i in range(n + 1) if i % 2 == 0)

print("#15:", sum_of_even(10))  # 30
