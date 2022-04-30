##Tema "Operadores Aritméticos"
'''   
    Sumar           (+)
    Restar          (-)
    Multiplicación  (*)
    Division        (/)
    Division Entera (//)
    Exponente       (**)
    Módulo          (%)
'''
#Suma
numOne = 10
numTwo = 20

result = numOne + numTwo + 10 + 20

print(result)

#Resta

result = numOne - numTwo

print('La resta de',numOne,'-',numTwo,'=',numOne - numTwo)

print(f'La resta de {numOne} - {numTwo} = {result}')

print('La resta de %d - %d = %d' % (numOne,numTwo,result)) 

print (5 + 8 - 7)

#Multiplicación

print(f'5 * 10 = {5 * 10}')

#Tener en cuenta prioridad de Operadores (potencias, raices, multiplicaciones, divisiones, sumas y restas)
print( 10 + 20 * 2 )
print( (10 + 20) * 2 )

#Potenciación
print(f'2 elevado a la 10 = {2**10}')

print( 2 + 4 - 3**3 * 5) #39, (-129), 16

#División
print(f'20 / 3 = {20/3}')
print(f'20 // 3 = {20//3}')


#Esto es un error
#print(20 / 0)


#Módulo o residuo
#10 % 3 --> Residuo = 1
print(f'El residuo de 10 dividido en 3 = {10%3}')
numOne = 50
numTwo = 30
print(f'El residuo de {numOne} dividido en {numTwo} = {numOne % numTwo}')

##Operadores de Comparación
'''
    Igualdad        (==)
    Diferente       (!=)
    Mayor que       (>)
    Mayor o Igual   (>=)
    Menor que       (<)
    Menor o Igual   (<=)
'''
#El resultado de evaluar una expresion logica es falso (False) o verdadero (True)
print(f'{numOne} > {numTwo}-->{numOne > numTwo}')
print(f'{numOne} < {numTwo}-->{numOne < numTwo}')
print(f'5>5-->{5>=5}')
print(f'5=5-->{5==5}')
print(f'5 diferente 5-->{5!=5}')


##Operadores Lógicos
'''
    and
    or
    not
    is
    is not
AND
    V y V = V
    V y F = F
    F y V = F
    F y F = F

OR
    V o V = V
    V o F = V
    F o V = V
    F o F = F
'''
valOne = 5
valTwo = 5
valThree = 10
ValFour = 15

print(f'{valOne}={valTwo} AND {valOne} > {ValFour} = {valOne == valTwo and valOne > ValFour}')

print(f'{valOne}={valTwo} OR {valOne} > {ValFour} = {valOne == valTwo or valOne > ValFour}')

print(not True)

print( 5 is 5)

print( 5 is not 6)

print ( 5 + 4 is 3 + 3 + 3 )

#Operadores de Asignación
'''
    =
    +=
    -=
    *=
    /=
    %=
    //=
'''

x = 10
x += 5 # x = x + 5

print(f'x={x}')

#x vale 15
x -= 10 # x = x - 10

#x ahora vale 5
print(f'x={x}')

x *= 10
#x ahora vale 50
print(f'x={x}')

print('*' * 10,'FIN DEL PROGRAMA','*' * 10)