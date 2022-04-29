import math

#Salida de datos
name = 'Jairo Armando'

age = 32

#print('Hola',name,'tienes',age,'años')

salary = 25000032

print(type(salary))

#Salida con formato
print('Hola %s tienes %d años y tu salario es %f' % (name,age,salary))

print('[%015.2f]' % (math.pi))

#Interpolacion de variables
print(f'Hola {name} tienes {age} años y el salario es {salary}')

#Entrada de Datos

name = input('Digite un Nombre ')

age = int(input('Digite la Edad '))

salary = float(input('Digite el Salario '))

print('Hola %s tienes %d años y el salario es %f' % (name,age,salary))

number = 34524

print('El numero %d en Octal=%o y en Hexadecimal=%x' % (number,number,number))







