#Estructuras de Datos
#Conjunto de datos que se identifican con un mismo nombre y que se pueden acceder en
#forma individual a cada elemento.

#Listas Enlazadas
##Sencilla, Dobles
##Pilas, Colas

lista = [345,75,43,9,34,29,17,9,643,9,12]

print(lista)

lista[2] = 456

print(lista)

print( lista[3] )

print(f'El Tamaño de la lista es {len(lista)}')

#Agregar Elementos

lista.append(129)  #Agrega al final de la lista

print(f'El Tamaño de la lista es {len(lista)}')

print(lista)

x = lista.pop() #Devuelve el último elemento de la lista y elimina el elemento

print(f'El valor de x={x}')

print(lista)

#Eliminar elemento
print('>>>>>>>>>>Ejemplo de Eliminar<<<<<<<<<<<<')
print(lista)
del lista[0]    #Elimina el Primer elemento de la lista (345)
del lista[-1]   #Elimina el Últumo elemento (12)

print(lista)

lista.remove(9)

print (lista)

#Iterar sobre las listas
print('<<<<<<<<<<Iterar sobre Listas>>>>>>>>>>>>')
for i in range(0,len(lista)):
    print(f'lista[{i}]={lista[i]}')

print('-'*20)

for i in lista:
    print( i )

numbers = [657,53,76,368,3525,75,87,12,8,2,88,25,21,69]

#Buscar Elemento.

find = eval(input('Elemento a Buscar'))

exists = False
for i in range(len(numbers)):
    if numbers[i] == find:
        print(f'El elemento se encuentra en la posicion %d ' % i )
        exists = True
        break

if not exists:
    print('El elemento %d no existe' % find )


suma = 0
for num in numbers:
    suma += num      #suma = suma + num

average = suma / len(numbers)

print(f'El Promedio es {average}')

#Hallar el número mayor de la lista 'numbers' en forma imperativa
higher = 0;
for num in numbers:
    if num > higher:
        higher = num

print(f'El Numero mayor es {higher}')

#Lo mismo (Hallar el Mayor, pero en forma declarativa)
print(f'El Mayor es {max(numbers)}')

#Serie de fibanacci --> 1 1 2 3 5 8 13 21 34 55 89 ...

fibo = [1,1]

for i in range(2,15):
    fibo.append(fibo[i-1] + fibo[i-2])

print( fibo )

#slicing. Permite acceder a un rango de elementos, se usan dos indices separados por dos puntos (:)
#El primer indice indica el primer elemento que se desea incluir, el segundo hasta donde (sin incluir)

numbers = list(range(1,101))

print(numbers)

print(numbers[5:7])

print(numbers[-1:-4])

print(numbers[0:10:2])

#filtrar los múltiplos de 3

multiplos = list();
for number in numbers:
    if number % 3 == 0:
        multiplos.append(number)

print(multiplos)

cousings = list()
for number in numbers:
    cont = 2;
    cousing = True
    while cont <= number // 2 and cousing:
        cousing = not( number % cont == 0 )
        cont += 1
    if cousing:
        cousings.append(number)

print(cousings)

del cousings[1]

borre = 654

if borre in cousings:
    cousings.remove(borre)

print(cousings)

#Generar números aleatorios. Se debe importar la libreria random
#random.randrange(n). Genera un aleartorio entre 0 y n-1
#random.randint(a,b). Genera un aleatorio entre a y b inclusive


#Ordenar, se usa el método sort sobre la lista
import random
unsorted = list()
for i in range(100):
    num = random.randint(1,1000)
    unsorted.append(num)

print( unsorted[:] )

sorted = unsorted[:]

sorted.sort()

print('-' * 80 )

print(sorted)

##Tuplas, es una colección que a diferencia de una lista es inmutable, no se pueden
#agregar, eliminar o modificar elementos

tupla = (456,678,25,89,567,[56,4,7])

print('La Tupla es ---->', tupla)

tupla[5][0] = 690

print('Ahora la Tupla es ---->', tupla)

print(f'La longitud de la tupla es %d' % len(tupla))

tp = tuple('MisionTIC 2022')

print(tp)
#Recorrer tuplas, igual que listas
#for i in tp:
#    print(i)

#Conjuntos

conjunto = set()

conjunto.add(2)
conjunto.add(5)
conjunto.add(1)
conjunto.add(2)

print( conjunto )

cnj = {24,67,35,76,5,'3'}

print(cnj)











