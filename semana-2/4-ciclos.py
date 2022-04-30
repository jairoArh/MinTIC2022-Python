#Estructuras de control repetitivas o iterativas

#while, ejecuta un conjunto de instrucciones, mientras el resultado de una condicion sea verdadero 
#Sintaxis ( while condicion: )

from calendar import c


x = 1

while x <= 5:
    print(x)
    x += 1

#Existen dos tipos de variables que son contador y acumulador
#contador - su valor cambia en un valor constante en cada iteración
#acumulador - su valor cambia en un valor diferentes en cada iteración

#Calculo de la Sumatoria de un Numero (5 = 1 + 2 + 3 + 4 + 5)
number = eval(input('Digite Numero '))
cont = 1
acum = 0

while cont <= number:
    acum = acum + cont  #acum += cont
    cont += 1

print(f'La Sumatoria de {number} es {acum}')

#Escribir un programa que calcule el factorial de un número (5! = 1x2x3x4x5=120 o 5! = 5x4x3x2x1=120)

#Escribir un programa que lea un número y visualice la suma de los números pares e impares que hay desde 
#1 hasta el número

cont = 1
acum_odd = 0
acum_pair = 0

while cont <= number:
    if cont % 2 == 0:
        acum_pair += cont
    else:
        acum_odd += cont
    cont += 1

print(f'La suma de Pares={acum_pair}\nLa suma de Impares={acum_odd}')

#Escribir un programa que lea dos numeros y visualice el número de múltiplos especificados en el segundo
#numero del primero (5, 4 -> 5 10 15 20)

#Romper un ciclo (break, continue)
#Escribir un Programa que lea un numero y visualice si es Primo o no es Primo

'''
while number != 0:

    number = eval(input('Digite Numero para Analizar si es Primo '))

    cont = 2
    cousing = True

    while cont <= number // 2 and cousing:
        cousing = not(number % cont == 0)
        cont += 1

    if cousing == True:         #Equivalente if cousing:
        print(f'El numero {number} es Primo')
    else:
        print(f'El numero {number} No es Primo') 

'''
#for - 
#Programa que halle los números primos desde 1 hasta el número leido, visualizar: los primos, cuantos hay 
#y cual es la suma (20--> 1, 2, 3, 5, 7, 11, 13, 17, 19; Hay 9 primos y la suma es 78)
number = eval(input('Digite Numero para Primos de 1 hasta numero '))

for x in range(1,number+1):
    print(x)


#Escribir un programa que lea un número y visualizar si el número leido es perfecto o no.
#Un número perfecto es aquel que la suma de sus divisores, excepto el mismo número, es igual al mismo número
#Ejemplos 
## 6 (1 + 2 + 3 = 6), 28, 496

#Escribir un programa que lea un número y visualice la suma de sus cifras (234536 --> 23)

#Escribir un programa que lea un número y lo visualice invertido (3546 --> 6453)




print('*' * 10,'FIN DEL PROGRAMA','*' * 10)