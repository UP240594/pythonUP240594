import random
import string


# 1. Barajar una lista
def shuffle_list(lista):
    lista_copia = lista[:]
    random.shuffle(lista_copia)
    return lista_copia

print("#7:", shuffle_list([1, 2, 3, 4, 5]))  # Ejemplo: [3, 1, 5, 2, 4]

# 2. Generar 7 números únicos entre 0 y 9
def unique_random_numbers():
    return random.sample(range(10), 7)

print("#8:", unique_random_numbers())  # Ejemplo: [0, 8, 3, 1, 7, 5, 6]
