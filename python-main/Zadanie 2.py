liczba_a = int(input("Podaj pierwszą liczbę: "))
liczba_b = int(input("Podaj drugą liczbę: "))

if liczba_b == 0:
    while liczba_b == 0:
        print("Nie dzielimy przez zero.")
        number_input = int(input('Podaj liczbę inną niż zero: '))
        if number_input != 0:
            liczba_b = number_input
            wynik = liczba_a / liczba_b
            print(wynik)
else:
    wynik = liczba_a / liczba_b
    print(wynik)