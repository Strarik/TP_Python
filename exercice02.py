def square(number):
    valeur = number * number
    return valeur

def run():
    assert square(1) == 1
    assert square(2) == 4
    assert square(3) == 9
    assert square(23) == 529
    assert square(-23) == 529
