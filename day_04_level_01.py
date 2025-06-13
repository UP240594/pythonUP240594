

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

print(cosas.split('  '))

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

