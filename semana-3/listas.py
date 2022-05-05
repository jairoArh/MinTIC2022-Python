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








