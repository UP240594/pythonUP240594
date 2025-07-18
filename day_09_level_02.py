#1
grade=int(input('Give me the grade'))

if grade >= 80 and grade<= 100:
   print('A')
elif grade >= 70 and grade <= 89:
   print('B')
elif grade >= 60 and grade <= 69:
   print('C')
elif grade >= 50 and grade <= 59:
   print('D')
else:
   print('F')
#2
month=input('Give me the month ').lower()

if month == 'september' or month == 'october' or month == 'november':
   print('The season is Autumn')
elif month == 'december' or month == 'january' or month == 'february':
   print('The season is winter')
elif month == 'march' or month == 'april' or month == 'may':
   print('The season is spring')
elif month == 'june' or month == 'july' or month == 'august':
   print('The season is summer')

#3

fruits = ['banana', 'orange', 'mango', 'lemon']
new_fruit=input('Give the fruit  ').lower()
is_there=new_fruit in fruits
if is_there == False :
   fruits.append(new_fruit)
   print('new list ', fruits)
else:
   print('That fruit already exist in the list')
