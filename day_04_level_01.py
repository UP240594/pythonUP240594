

#1

l1='Thirty '
l2=' Days '
l3=' Of '
l4=' Python '
sentence=l1 + l2 + l3 + l4

print(sentence)

#2

c= 'Coding '
f= ' For '
a=' All '
cfa=c + f + a

print(cfa)

#3

company='Coding For All'

#4

print(company)

#5

print(len(company))

#6

print(company.upper())

#7

print(company.lower())

#8

capitalize=company.capitalize()
title=company.swapcase()
swapcase=company.swapcase()
print(capitalize , title , swapcase) 


#9

slice= company[company.find(' ')+1:]
print(slice)

#10

popo=company.find("Coding")

print(popo)

#11

print(company.replace("Coding For All" , " Python "))

#12

palabra='Python For Everyone'

print(palabra.replace('For Everyone' , 'For All'))

#13

print(palabra.split(' '))

#14

cosas="Facebook  ,Google , Microsoft , Apple , IBM , Oracle, Amazon"

print(cosas.split(' , '))

#15

print(company[0])

#16

print(company[-1])

#17

print(company[10])

#18

xd=palabra.split()

primero=xd[0][0].upper()
segundo=xd[1][0].upper()
tercero=xd[2][0].upper()

poposs=primero+segundo+tercero

print(poposs)


#19 me quede en el 19

palabra2='Coding For All'

splits=palabra2.split()

p1=splits[0][0].upper()
p2=splits[1][0].upper()
p3=splits[2][0].upper()

print(p1 + p2 +p3)

#20

print(palabra2.index('C'))

#21

print(palabra2.index('F'))


#22


word='Coding For All People'

print(word.rfind('l'))

#23

sentences='You cannot end a sentence with because because because is a conjunction'

print(sentences.index('because'))

#24

print(sentences.rindex('because'))

#25



print(sentences.replace('because because because', '').strip())


#26

print(sentences.index('because'))

#27

print(sentences.replace('because','').strip())

#28


print(palabra2.startswith('Coding'))

#29
print(palabra2.endswith('Coding'))
#30
pp='   Coding For All      ' 
print(pp.replace('   ','').strip())
#31
variable1='30DaysOfPython'
variable2='thirty_days_of_python'
print(variable1.isidentifier())
print(variable2.isidentifier())
#The variable that returns true is thirty_days_of_python

#32
lists=['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
result=' / '.join(lists)
print(result)
#33
texto=print( 'I am enjoying this challenge. \n I just wonder what is next')
#34

print('I hope everyone is enjoying the Python Challenge.\nAre you ?') # line break
print('Name\tAge\tCountry\tCity') # adding tab space or 4 spaces 
print('Asabeneh\t250\tFinland')
print('Helsinki\t\t')
#35


first_name = 'Olivia'
last_name = 'Chairez'
language = 'Python'
formated_string = 'I am {} {}. I teach {}'.format(first_name, last_name, language)
print(formated_string)
a = 10
b = (3,14 * a ** 2 )


print('The area Of the Circle with radius {} is {} '.format( a ,  b))


#36

a=8
b=6

print('{}+{} = {}'.format(a,b,a+b))
print('{}-{} = {}'.format(a,b,a-b))
print('{}*{} = {}'.format(a,b,a*b))
print('{}/{} = {}'.format(a,b,a/b))
print('{}%{} = {}'.format(a,b,a%b))
print('{}//{} = {}'.format(a,b,a//b))
print('{}**{} = {}'.format(a,b,a**b))

