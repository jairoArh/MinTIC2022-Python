from inspect import Attribute


def is_cousing(num):
    if isinstance( num, int ):
        cont = 2
        cousing = True
        while cont <= num / 2 and cousing:
            cousing = not( num % cont == 0 )
            cont += 1
        
        return cousing
    
    raise TypeError('[is_cousing]El tipo de dato del parámetro no es un entero')

def get_digits(n): 
    if isinstance( n, int ):
        cont = 0
        while n > 0:
            cont += 1
            n //= 10
        
        return cont
    
    raise TypeError('[get_digits]El tipo de dato del parámetro no es un entero')

def invert(num):
    if isinstance(num, int):

        aux = 0
        while num >= 1:
            r = num % 10
            aux = aux * 10 + r
            num //= 10

        return aux
        #return str(num)[::-1]

    raise TypeError('[invert]El tipo de dato del parámetro no es un entero')

def erase_spaces(chain):
    return chain.replace(' ','')

def is_palindromo(chain):
    
    if isinstance(chain,str):

        chain_invert = erase_spaces(chain[::-1]).upper()
        
        return chain_invert == erase_spaces(chain).upper()

    raise TypeError('[is_palindromo]El argumento no es una cadena')

def is_numeric(l):

    for element in l:
        if not isinstance(element,int):
            return False

    return True

def calc_avg(vec):
    if isinstance(vec,list):
        if is_numeric(vec):
            sum = 0
            for num in vec:
                sum += num
            
            return sum / len(vec)

        raise AttributeError('[calc_avg]Elemento de lista no es válido')
    
    raise TypeError('[calc_avg]El argumento no es una lista')

'''
5! = 5 * 4!
4! = 4 * 3!
3! = 3 * 2!
2! = 2 * 1!
'''

def factorial(n):
    if n == 0 or n == 1:
        return 1
    
    return n * factorial(n - 1)


def get_combinations(n,r):
    if isinstance(n,int) and isinstance(r,int):

        return factorial(n) / ( factorial(r) * factorial(n-r))

    raise TypeError('[get_combinatios]Valor de argumento no es un numero')