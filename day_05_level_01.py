#1
empty= []
#2
lista=['popo','kk','menso','ola','qwert','ikuj']
#3
print(len(lista))
#4
print(lista[0], lista[3],lista[5])
#5
mixed_data_types=['olivia', 18 , 1.68,'solter',178]
#6
it_companies=['Facebook','Google','Microsoft','Apple','IBM', 'Oracle','Amazon']
#7
print(it_companies)
#8
print(len(it_companies))
#9
middle=len(it_companies) //2
print(middle)
print(it_companies[0],it_companies[middle],it_companies[6])
#10
it_companies[2]='Xampp'
print(it_companies)
#11
it_companies.insert(4,'Brave')
print(it_companies)
#12
it_companies.insert(4,'Office')
print(it_companies)
#13
it_companies.remove('IBM')
print(it_companies)
#14
popos='#;  '.join(it_companies)
print(popos)
#15
popo= 'Facebook' in it_companies
print(popo)
#16
it_companies.sort(reverse=True)
print(it_companies)
#17

