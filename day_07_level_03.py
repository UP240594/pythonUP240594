
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]


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
valorSinreducir=len(splited)
splitedReal=valorSinreducir-1
print(splitedReal, ' Es su valor real')


