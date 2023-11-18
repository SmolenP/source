
finish_loop_sign = 'y'
z = 0
while finish_loop_sign != 'x':
    number_input = input('Podaj liczbę: ')
    if number_input == 'x':
        finish_loop_sign = 'x'
    else :
        z = z + int(number_input)
        
print(z)