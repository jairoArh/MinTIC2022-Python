
def is_cousing(num):
    cont = 2
    cousing = True
    while cont <= num / 2 and cousing:
        cousing = not ( num % cont == 0)
        cont += 1

    return cousing

def load_data():
    num_one = eval(input('Numero Uno...: '))
    num_two = eval(input('Numero Dos...: '))

    hihger = num_one if num_one > num_two else num_two
    less = num_one if num_one < num_two else num_two

    return less,hihger

if __name__ == '__main__':

    num_one, num_two = load_data()

    for num in range(num_one,num_two+1):
        if is_cousing(num) == True:
            print( num )