
def menu_numpy():
    option_numpy = '1'
    while option_numpy != '0':
        menu_numpy = '''
             <<<<<<<<<MENU numpy>>>>>>>>
                    1. Generar Matriz con aleatorios
                    2. Funcion 2 numpy
                    0. Salir
            ''' 
        print(menu_numpy)
        option_numpy = input('Digite su Opcion.. ')
        if option_numpy == '1':
            rows = eval(input('Numero de Filas..: '))
            cols = eval(input('Numero de Columnas..: '))
            print(f'Filas={rows}\nColumas={cols}')
        elif option_numpy == '2':
            print('Opcion 2 de numpy')

def menu_pandas():
    print('Menu Pandas')

def main_menu():
    exited = False

    while not exited:
        main_menu = '''
            <<<<<<<<<MENU PRINCIPAL>>>>>>>>
                1. Funciones con numpy
                2. Funciones con pandas
                3. Salir
        '''
        print (main_menu);
        option = input('Seleccione Opcion ')

        if option == '1':
            menu_numpy()

        elif option == '2':
            menu_pandas()

        elif option == '3':
            exited = True
        else:
            print ('Opcion No Válida')


if __name__ == '__main__':
    main_menu()