'''
Funciones: Una función es un bloque de código que realiza una tarea específica.
Las funciones pueden retornar un valor, en el caso de Python más de uno. 
La sentencia return permite retornar el valor al programa, y finalizar la
ejecución de la función. Una función puede tener varios return, pero, condicionados (if)

Una función se define con la palabra reservada def nombreFuncion(parametros)
los parámetros pueden ser formales o locales

Para realizar el llamado a una función se hace a través del nombre de la función
y se deben indicar los parámetros locales

La implementación de una función se debe realizar antes de su llamado


'''

from time import clock_settime

def sum(num_one, num_two):

    return num_one + num_two

def is_even(x):
    
    return x % 2 == 0
    

#-------------------------------------------------------------------
#Función principal del Programa (main)
#-------------------------------------------------------------------
if __name__ == '__main__':

    print('Hello World!!')


    num_one = eval(input('Numero Uno..: '))
    num_two = eval(input('Numero Dos..: '))

    sum(20, 30)


    print(f'La suma de {num_one} + {num_two} = {sum(num_one, num_two)}')

    if is_even(num_two):
        print(f'El  numero {num_two} Es PAR')
    else:
        print(f'El  numero {num_two} Es IMPAR')



#-----------------------------------------------------------------------   

