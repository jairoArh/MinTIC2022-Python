from tools import *
import pytest 

def test_if_cousing():
    assert is_cousing(1) == True
    assert is_cousing(2) == True
    assert is_cousing(13) == True
    assert is_cousing(4) == False
    assert is_cousing(11) == True
    assert is_cousing(49) == False

    with pytest.raises(TypeError):
        is_cousing('34')


def test_get_digits():
    assert get_digits(25435) == 5
    assert get_digits(2) == 1
    assert get_digits(25) == 2
    assert get_digits(254) == 3
    assert get_digits(2543) == 4

    with pytest.raises(TypeError):
        get_digits('34')

def test_invert():
    assert invert(1654) == 4561
    assert invert(123) == 321
    assert invert(489632) == 236984
    assert invert(14) == 41

def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(3) == 6
    assert factorial(4) == 24
    assert factorial(5) == 120
    assert factorial(6) == 720

def test_get_combinations():
    assert get_combinations(4,2) == 6
    assert get_combinations(5,3) == 10
    assert get_combinations(6,2) == 15
    with pytest.raises(TypeError):
        get_combinations(6,'2')

def test_calc_avg():
    assert calc_avg([1,2,3]) == 2
    assert calc_avg([25,48,35]) == 36
    assert calc_avg([12,45,96,23,14]) == 38

    with pytest.raises(TypeError):
        calc_avg(5)
    
    with pytest.raises(TypeError):
        calc_avg('5')

    with pytest.raises(AttributeError):
        calc_avg([4,6,8,'7',9])
        








