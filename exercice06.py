def factorial(number):
    value = 1
    negative = False

    if number < 0 :
        number = -number
        negative = True
    elif number == 0 :
        return 0
    
    for i in range(number) :
        value = (i+1) * value
    
    if negative :
        value = -value

    return value

def run():
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(3) == 6
    assert factorial(4) == 24
    assert factorial(8) == 40320
    assert factorial(-8) == -40320