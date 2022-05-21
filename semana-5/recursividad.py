from signal import pause


def do_mult(multiplicando, multiplicador):
    if multiplicador == 1:
        return multiplicando

    return multiplicando + do_mult(multiplicando, multiplicador-1)

def do_div(num_one, num_two):
   #TODO

   pass

def do_fact(n):
    if n == 1 or n == 0:
        return 1
    return n * do_fact(n-1)

def do_mcd( dividendo, divizor):
    if dividendo % divizor == 0:
        return divizor

    return do_mcd( divizor, dividendo % divizor )

def do_pow( fix, pow ):
    if pow == 0:
        return 1
    
    return fix * do_pow(fix, pow - 1)

def mult():
    num_one = eval(input('Numero Uno..: '))
    num_two = eval(input('Numero Dos..: '))
    print(f'La Multiplicacion de {num_one} y {num_two} = {do_mult(num_one,num_two)}')

def div():
    #TODO leer dos números y visualizar el resultado del llamado a la función respectiva
    do_div(3,4)

def pow():
    fix = eval(input('Base..: '))
    pow = eval(input('Potencia..: '))

    print(f'{fix} elevado a la {pow} es {do_pow(fix,pow)}')

def sum():
    #TODO leer un número y vualizar el resultado de la función que calcula la sumatoria del numero
    pass

def fact():
   num = eval(input('Numero...: '))
   print(f'El Factorial de {num} es {do_fact(num)}')

def mcd():
    num_one = eval(input('Numero Uno..: '))
    num_two = eval(input('Numero Dos..: '))
    print(f'El MCD de {num_one} y {num_two} es {do_mcd(num_one,num_two)}')

def do_fibo(n):
    if n == 1 or n == 2:
        return 1
        
    return do_fibo(n-1) + do_fibo(n-2)


def fibo():
    # 1 1 2 3 5 8 13 21 34 55 89 144 233
    # 1 2 3 4 5 6 7  8  9  10 11 12  13
   num = eval(input('Elemento de Fibonacci...: '))
   print(f'el {num}-esimo término es {do_fibo(num)}')

def cousing():
    #TODO leer un número y visualizar un mensaje que indique si el número es primo o no dependiendo del llamado a la respectiva función
    pass


def main_menu():
    exited = False

    while not exited:
        main_menu = '''
            <<<<<<<<<MENU PRINCIPAL>>>>>>>>
                1. Multiplicar
                2. Dividir
                3. Potencia
                4. Sumatoria
                5. Factorial
                6. Maximo Común Divisor
                7. e-nésimo Fibonacci
                8. Numero Primo
                0. 'Salir'
        '''
        print (main_menu);
        option = input('Seleccione Opcion ')

        if option == '1':
           mult()

        elif option == '2':
            div()

        elif option == '3':
            pow()
        
        elif option == '4':
            sum()

        elif option == '5':
            fact()

        elif option == '6':
            mcd()

        elif option == '7':
            fibo()

        elif option == '8':
            cousing()

        elif option == '0':
            exited = True

        else:
            print ('Opcion No Válida')

if __name__ == '__main__':
    main_menu()