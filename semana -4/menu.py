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
        option_numpy = '1'
        while option_numpy != '0':
            menu_numpy = '''
                <<<<<<<<<MENU PRINCIPAL>>>>>>>>
                    1. Funcion 1 numpy
                    2. Funcion 2 numpy
                    0. Salir
            ''' 
            print(menu_numpy)
            option_numpy = input('Digite su Opcion.. ')
            if option_numpy == '1':
                print('Opcion 1 de numpy')
            elif option_numpy == '2':
                print('Opcion 2 de numpy')

    elif option == '2':
        print('opciones pandas')

    elif option == '3':
        exited = True
    else:
        print ('Opcion No Válida')
