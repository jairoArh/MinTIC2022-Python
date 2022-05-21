from signal import pause


def do_mult(num_one, num_two):
    result = num_one * num_two

    return result

def do_div(num_one, num_two):
    #TODO calcula y retorna la division del numero y mayor entre el menor
    pass


def mult():
    num_one = eval(input('Numero Uno..: '))
    num_two = eval(input('Numero Dos..: '))
    print(f'La Multiplicacion de {num_one} y {num_two} = {do_mult(num_one,num_two)}')

def div():
    #TODO leer dos números y visualizar el resultado del llamado a la función respectiva
    pass

def pow():
    #TODO leer la base y la potencia y visualiza el resultado del llamado a la función respectiva
    pass

def sum():
    #TODO leer un número y vualizar el resultado de la función que calcula la sumatoria del numero
    pass

def fact():
    #TODO leer un número y vualizar el resultado de la función que calcula el factorial del numero
    pass

def mcd():
    #TODO leer dos números y visualizar el resultado de la función que calcula el MCD de los dos numeros
    pass

def fibo():
    #TODO leer un número n y visualizar el n-esimo término de la serie de fibonacci
    pass

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