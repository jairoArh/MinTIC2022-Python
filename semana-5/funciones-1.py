#Programa que halla los números primos desde un numero menor hasta uno mayor
#definidos por el usuario, en un solo bloque

num_one = eval(input('Numero Uno.. '))
num_two = eval(input('Numero Dos.. '))

'''if num_one > num_two:
    hihger = num_one
    less = num_two
else:
    hihger = num_two
    less = num_one'''

hihger = num_one if num_one > num_two else num_two

less = num_one if num_one < num_two else num_two

#print(f'El Mayor es {hihger}, el Menor es {less}')

for num in range(less,hihger+1):
    cont = 2
    cousing = True
    while cont <= num / 2 and cousing:
        cousing = not( num % cont == 0 )
        cont += 1
    
    if cousing:
        print(num)
