
#Declarando numeros
age=18;
height=1.68;
complex_number=2+3j;

#Area de un triangulo

b=float(input("Dame la base"));
h=float(input("Dame la altura"));

area=0.5*b*h;

print("The area of the triangle is: ", area);

#Perimetro de un triangulo

a=float(input("Give me the side A of the triangle:  "));
b=float(input("Give me the side B of the triangle: "))
c=float(input("Give me the side C of the triangle: "))

perimeter=a+b+c

print("The perimeter of the triangle is: ", perimeter);

#Area de un rectangulo

width=float(input("Give me the with of te rectangle "));
length=float(input("Give me the lenght of te rectangle "))

area_Rectangle=length*width
perimeter_rectangle=2*(length+width)

print("The area and perimeter of the rectangle is: " , area_Rectangle , "And the perimeter " , perimeter_rectangle)

#Radio de circulo 

pi=3.1416

r=float(input("Give me the radius of the circle "));

area_circle=pi*r*r;
circuference=2*pi*r

print("The area is: ", area_circle , "And the circuference: " , circuference)

#Pendiente

m=2
b=-2
#mx+b=0
#mx=-b
#x=-b/m
x=-b/m
print("X is: ", x)

#Calcular pendiente
y2=10
y1=2
x1=2
x2=6

m=y2-y1/x2-x2
print("La pendiente es ", m )


#Comparativa

"""Los resultados dados son muy diferentes debido a que
en el ejercicio 8 ya nos dan en si mismo una ecuacion resuelta
y nosotros podiamos sacar el valor de x
que es donde se insersectaba la pendiente

mientras que en el 10 debiamos calcular la pendiente
desde 0 pidiendo los datos, asi dandonos

1 en el 8
y en el 9 3.6"""


#Calcular que valor de x me da 0

x=int(input("Dame un valor para x"));
y=x**2 + 6*x + 9

print("El valor de y fue de: " , y )

#el valor -3 da cero
print("Valor de caracteres de python")
python="python"
dragon="dragon"
print(len(python))
print(len(dragon))
#ambos tienen 6 en sus caracteres

#Revisar operadores

print(len('python') == len('dragon'))
sentence='I hope this course is not full of jargon'
print('jargon' in sentence)

#on
print( 'on' in python )
print( 'on' in dragon )

#convertir valores
lenof=(len(python))
floats=(float(lenof))
string=(str(floats))

print("Longitud ", lenof)
print("Numero " , floats)
print("str " , string)
#divisibles de 2

n=float(input("Dame un numero"))
d=n%2
print ('tiene residuo de cero?')
print (d == 0 )


#18

number=7 // 3

print( number == int(2.7))

#19

print('10' == type(10))

#20

print(int(9.8) == type(10))

#21

hr=float(input("Dame las horas que trabajas"))
h=float(input("Cuanto ganas por hora?"))

pago=hr*h

print("Ganaste " , pago)


#22

y=float(input ("Enter number of years you have lived"))

years=y*31557600

print("You have lived for" , years , "seconds")

#23

print ("1 1 1 1 1")
print('2 1 2 4 8')
print('3 1 3 9 27')
print('4 1 4 16 64')
print('5 1 5 25 125')


#Termine el dia 3