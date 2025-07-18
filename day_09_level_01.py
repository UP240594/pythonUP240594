#1

x=int(input('Enter your age: '))
if x >= 18:
    print('You are old enough to drive.')
else:
    print('wait for the missing amount of years')

#2
my_age=int(input('my age is: '))
your_age=int(input('enter your age: '))

if my_age > your_age:
    omg= my_age-your_age
    print('Te gano por', omg , 'anos')
elif my_age == your_age:
    print('Tenemos la misma edad')
else:
    omg=your_age-my_age
    print('You are' , omg , 'years older than me.')
    
#3
one=int(input('Enter number one'))
two=int(input('Enter the numbre two'))

if one > two:
    print(one ,'Is greater than ' , two)
elif one == two:
    print(one,'is equal to ',two)

else:
    print(one,'is smaller than ', two)

