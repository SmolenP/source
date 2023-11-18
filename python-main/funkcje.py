def check(b):
    if b%2 == 0:
        return b * 2
    else:
        return b / 5
    
def func(input):
    check_result = check(input)
    print(check_result)
    return check_result - 2
    
a =int(input('Podaj liczbę: '))
print(func(a))