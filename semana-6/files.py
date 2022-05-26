#Para manipulación de archivos en Python, el interprete nos provee de varias 
#funciones (open(), close())

#Abrir archivo se especifica el nombre del archivo y el modo de apertura
'''
    r -> Solo Lectura
    w -> Escritura, si el archivo no existe, lo crea; si existe lo sobreescribe
    a -> Agregar al final del archivo
    r+ -> Lectura/Escritura No sobreescribe
    w+ -> Lectura/Escritura Sobreescribe
    a+ -> Lectura/Escritura No sobreescribe
'''

fd = open('Frankenstein.txt','r')

#print(type(fd))

data = fd.readlines()

vec = fd.read().split("\n")

print(data)

for line in vec:
    print(line)

fd.close()
