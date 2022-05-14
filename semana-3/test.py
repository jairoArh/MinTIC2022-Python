sw = True
while sw:
    num = eval(input('Digite Numero..: '))
    num *= 2

    print(f'El Valor ahora es %d' % num )
    resp = input('Desea Leer otro Numero [S/N] ')
    if resp.upper() == 'S':
        other = eval(input('Digite otro valor..: '))
        print('El producto de %d x %d = %d' % (num,other,num*other))
    else:
        sw = False

print('fin del programa')

'''
8   1   6
3   5   7
4   9   2
'''
