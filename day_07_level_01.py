
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
#1
print(A .union(B))
#2
print(A.intersection(B))
#3
print(A.issubset(B))
#4
print(A.issubset(B))
#5
print(A.union(B))
#6
print(A.symmetric_difference(B))
#7

del A
del B
del age


'''      Excercises Level 3    '''

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#1
age1= {22, 19, 24, 25, 26, 24, 25, 24}
print( len(age) ,len(age1) )
#The set that have the biggest len is the list

#2

# La diferencia ente string es la siguiente:
#Es que es tipo caracter, o letra pueden ser letras incluso chinas
#La lista es un conjunto de caracteres como una lista del mercado
#el tuple es una lista que no se puede modificar
#el set es un tipo de listsa en el que se pueden sacar intersecciones unionen o diferencias simetricas

#3
randomWord='I am a teacher and I love to inspire and teach people. '
splited=randomWord.split()
print(len(splited))



