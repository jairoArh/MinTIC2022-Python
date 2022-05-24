'''
Libreria de Python que contiene funciones que se pueden usar en varios
programas
'''

def do_fact(n):
    '''
        Función que calcula el factorial de un número que se recibe como parámetro
        input
            El número al que se le va a calcular el factorial
        output
            El factorial del valor del parámetro
    '''
    if n == 1 or n == 0:
        return 1
    return n * do_fact(n-1)

def do_mcd( dividendo, divizor):
    if dividendo % divizor == 0:
        return divizor

    return do_mcd( divizor, dividendo % divizor )
