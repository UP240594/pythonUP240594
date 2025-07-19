import random
import string

# 1. Generar un ID aleatorio de 6 caracteres
def random_user_id():
    caracteres = string.ascii_letters + string.digits
    return ''.join(random.choices(caracteres, k=6))

print("#1:", random_user_id())  # Ejemplo: 'a1B2cD'

# 2. Generar múltiples IDs aleatorios con longitud y cantidad dadas por el usuario
def user_id_gen_by_user():
    longitud = int(input("Ingresa la longitud del ID: "))
    cantidad = int(input("Ingresa la cantidad de IDs a generar: "))
    caracteres = string.ascii_letters + string.digits
    ids = [''.join(random.choices(caracteres, k=longitud)) for _ in range(cantidad)]
    return '\n'.join(ids)



# 3. Generar un color en formato rgb
def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r},{g},{b})"

print("#3:", rgb_color_gen()) 