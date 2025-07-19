#1 Suma de dos números
def sumar_dos_numeros(a, b):
    return a + b

#2 Área de un círculo
import math
def area_circulo(radio):
    return math.pi * radio * radio

#3 Sumar todos los números, validando que sean numéricos
def sumar_todos_numeros(*args):
    for valor in args:
        if not isinstance(valor, (int, float)):
            return "Error: Todos los elementos deben ser números"
    return sum(args)

#4 Convertir Celsius a Fahrenheit
def convertir_celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

#5 Determinar estación según el mes
def verificar_estacion(mes):
    mes = mes.lower()
    if mes in ['septiembre', 'octubre', 'noviembre']:
        return 'Otoño'
    elif mes in ['diciembre', 'enero', 'febrero']:
        return 'Invierno'
    elif mes in ['marzo', 'abril', 'mayo']:
        return 'Primavera'
    elif mes in ['junio', 'julio', 'agosto']:
        return 'Verano'
    else:
        return 'Mes inválido'

#6 Calcular pendiente de una recta dados dos puntos (x1, y1), (x2, y2)
def calcular_pendiente(x1, y1, x2, y2):
    if x2 == x1:
        return 'Pendiente indefinida (división por cero)'
    return (y2 - y1) / (x2 - x1)

#7 Resolver ecuación cuadrática ax^2 + bx + c = 0
import math
def resolver_cuadratica(a, b, c):
    discriminante = b**2 - 4*a*c
    if discriminante < 0:
        return "No hay soluciones reales"
    x1 = (-b + math.sqrt(discriminante)) / (2*a)
    x2 = (-b - math.sqrt(discriminante)) / (2*a)
    return x1, x2

#8 Imprimir cada elemento de una lista
def imprimir_lista(lista):
    for elemento in lista:
        print(elemento)

#9 Invertir una lista usando bucle
def invertir_lista(lista):
    lista_invertida = []
    for elemento in lista:
        lista_invertida.insert(0, elemento)
    return lista_invertida

#10 Capitalizar los elementos de una lista
def capitalizar_lista(lista):
    return [elemento.capitalize() for elemento in lista]

#11 Agregar un elemento al final de una lista
def agregar_elemento(lista, elemento):
    lista.append(elemento)
    return lista

#12 Remover un elemento de una lista
def remover_elemento(lista, elemento):
    if elemento in lista:
        lista.remove(elemento)
    return lista

#13 Sumar números del 1 hasta n
def suma_numeros(n):
    return sum(range(1, n+1))

#14 Sumar todos los números impares desde 1 hasta n
def suma_impares(n):
    suma = 0
    for numero in range(1, n+1):
        if numero % 2 != 0:
            suma += numero
    return suma

#15 Sumar todos los números pares desde 1 hasta n
def suma_pares(n):
    suma = 0
    for numero in range(1, n+1):
        if numero % 2 == 0:
            suma += numero
    return suma