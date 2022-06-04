from tools import *

try:
    print(is_cousing(9))
    print(get_digits(145673465))
    print(invert(6463))
    print( is_palindromo('Yo Hago YOGA Hoy')) 
    print(calc_avg([4,3,2,'6']))
except (TypeError,AttributeError) as e:
    print(e)

print('>>>>>>>>>>>>>>Fin del Programa<<<<<<<<<<<<<<')