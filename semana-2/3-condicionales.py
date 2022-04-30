##Tema Operadores Condicionales
'''
    El si condicional es if ()
'''

x = eval(input('Digite un Numero '))

if x % 2 == 0:
    print(f'El Numero {x} es Par')
else:
    print(f'El Numero {x} es Impar')

if x > 10:
    print(f'{x} Mayor que 10')

name = input('Digite Nombre ')
age = eval(input('Digite la Edad'))

if age >= 18:
    print(f'{name} eres un Adulto')
else:
    print(f'{name} eres Menor de Edad')
    
print('*' * 10,'FIN DEL PROGRAMA','*' * 10)