import string

def encriptador(mensaje):

    lista = list(mensaje)

    join = dict(zip(lista,string.ascii_uppercase))

    return join, 'Hola '

def desencriptador(encriptado, clave):

    return encriptado, clave
    

if __name__ == '__main__':
    one, dos = encriptador('Hello World!!')

    print( desencriptador(one, dos))

