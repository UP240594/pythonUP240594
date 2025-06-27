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
print(it_companies[2].upper())
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
it_companies.reverse()
print(it_companies)
#18
p=it_companies[:3]
print(p)
#19
p=it_companies[-3:]
print(p)
#20
i=it_companies[3:-3]
print(i)
#21
it_companies.remove('Facebook')
print(it_companies)
#22
middles=it_companies[3:-3]
it_companies.remove('Google')
print(it_companies)
#23
last=it_companies[0:5]
it_companies.remove('Xampp')
print(it_companies)
#24
it_companies.clear()
print(it_companies)
#25
del it_companies
#26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
join=front_end + back_end
print(join)
#27
full_stack=front_end + back_end
full_stack.insert(5, 'Python')
full_stack.insert(6, 'SQL')
print(full_stack)