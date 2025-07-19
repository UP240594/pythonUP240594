#1
count=0
while count < 10:
    count=count+1
    print(count, 'xd')
#2
count=10
while count > 0:
    print(count)
    count=count-1
#3
value = '#'
count = 0
while count < 7:
    count = count + 1
    print('{}'.format(value))
    value = value + '#'
#4
for row in range(8):          
    for col in range(8):      
        print('#', end=' ')   
    print()
#5
for i in range(11):
    print(f"{i} x {i} = {i * i}")

#6
techs = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for tech in techs:
    print(tech)

#7
for i in range(0, 101):
    if i % 2 == 0:
        print(i)

#8
for i in range(0, 101):
    if i % 2 != 0:
        print(i)





    