
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
'''Exercises level 1'''
#1
print(len(it_companies))
#2
it_companies.add('Twitter')
print(it_companies)
#3
it_companies.update(['Tesla','Oracle','Linux'])
print(it_companies)
#4
it_companies.remove('IBM')
print(it_companies)
#5
'''El metodo remove elimina una un elemento
de la lista si es que existe, sin o existe va a generar
errores por lo que si no sabes si existe el elemento
es mejor usar discard, que no generara errores'''

'''Exercises level 2'''

