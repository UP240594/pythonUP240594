
#variables

sisters=('Daniela','Mariana')
brothers=('Pepe','Popo')
siblings=sisters+brothers
parents=('Mama','Papa')
family_members=siblings+parents



'''Level 2'''

#1
hermanas=family_members[0:2]
hermanos=family_members[2:4]
papas=family_members[4:6]
print(hermanas , hermanos , papas)
#2
fruits=('Melon','Guayaba','Apple')
vegetables=('Chile','Pepino','Carrot')
animal_products=('Milk','Steak','Eggs')
food_stuff_tp=fruits+vegetables+animal_products
print(food_stuff_tp)
#3
food_stuff_lt=list(food_stuff_tp)
print(food_stuff_lt)
#4
print(len(food_stuff_lt))
middle=len(food_stuff_lt) // 2
print(middle)
middle2=middle+1
print(food_stuff_lt[middle],food_stuff_lt[middle2])
#5
print(food_stuff_lt[0:3] , food_stuff_lt[0:-6])
#6
del food_stuff_tp
#7
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)
#Termine 