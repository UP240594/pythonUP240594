import random
import string
def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r},{g},{b})"


# 1. Lista de colores hexadecimales
def list_of_hexa_colors(n):
    colores = []
    for _ in range(n):
        color = '#' + ''.join(random.choices('0123456789abcdef', k=6))
        colores.append(color)
    return colores

print("#4:", list_of_hexa_colors(3))  # Ejemplo: ['#a1b2c3', '#4f5e6d', '#abcdef']

# 2. Lista de colores RGB
def list_of_rgb_colors(n):
    return [rgb_color_gen() for _ in range(n)]

print("#5:", list_of_rgb_colors(3))  # Ejemplo: ['rgb(123, 45, 67)', ...]

# 3. Generador general de colores
def generate_colors(tipo, cantidad):
    if tipo == 'hexa':
        return list_of_hexa_colors(cantidad)
    elif tipo == 'rgb':
        return list_of_rgb_colors(cantidad)
    else:
        return "Tipo de color no válido. Usa 'hexa' o 'rgb'."

print("#6:", generate_colors('hexa', 3))  # Ejemplo: ['#a3e12f', '#03ed55', '#eb3d2b']
print("#6:", generate_colors('rgb', 2))   # Ejemplo: ['rgb(15, 26, 80)', 'rgb(99, 204, 11)']
