fd = open('./semana-6/numbers.txt','r')

numbers = fd.readlines()

for line in numbers:
    print(f'Contenido={line} Tipo-->{type(line)}')