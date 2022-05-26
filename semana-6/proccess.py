
try:
    fd = open('./semana-6/frase.txt','r')


    #lista = fd.readlines()

    data = fd.read().split("\n")

    print('*'*50)
    print(data)
    print('*'*50)
    print(f'Tamaño {len(data)}')

    for line in data:
        print(line)

    print(type(data))

    

    fd.close()
except FileNotFoundError:
    print('Error')

print('Fin del programa')
