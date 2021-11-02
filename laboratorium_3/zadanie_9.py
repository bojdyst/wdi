#PIN = 1234
saldo = 0

while True:
    pin = input("Witamy w bankomatach PythonCash! Proszę podać PIN: ")
    if pin == "1234":
        dzialanie = input("Wybierz działanie na koncie. Wpisz: Wypłata/Wpłata/Saldo: ")
        if dzialanie == "Wypłata":
            wyplata = int(input("Wprowadź wypłacaną kwotę: "))
            if wyplata > saldo:
                print("Nie masz na tyle środków :(")
            else:
                saldo -= wyplata
        elif dzialanie == "Wpłata":
            wplata = int(input("Wprowadź wpłacaną kwotę: "))
            saldo += wplata
        elif dzialanie == "Saldo":
            saldo
        print("Saldo konta wynosi: ", saldo)

        ponowienie = input("Czy chcesz zakończyć operację? Wpisz T/N: ")
        if ponowienie == "T":
            print("Dziękujemy za skorzystanie z usłóg PythonCash. Zapraszay ponownie!")
            break
    
    else:
        proba = input("PIN niepoprawny, masz jeszcze jedną próbę: ")
        if proba == "1234":
            dzialanie = input("Wybierz działanie na koncie. Wpisz: Wypłata/Wpłata/Saldo: ")
            if pin == "1234":
                dzialanie = input("Wybierz działanie na koncie. Wpisz: Wypłata/Wpłata/Saldo: ")
            if dzialanie == "Wypłata":
                wyplata = int(input("Wprowadź wypłacaną kwotę: "))
                if wyplata > saldo:
                    print("Nie masz na tyle środków :(")
                else:
                    saldo -= wyplata
            elif dzialanie == "Wpłata":
                wplata = int(input("Wprowadź wpłacaną kwotę: "))
                saldo += wplata
            elif dzialanie == "Saldo":
                saldo
            print("Saldo konta wynosi: ", saldo)

            ponowienie = input("Czy chcesz zakończyć operację? Wpisz T/N: ")
            if ponowienie == "T":
                print("Dziękujemy za skorzystanie z usłóg PythonCash. Zapraszay ponownie!")
                break
        else:
            print("PIN niepoprawny, prosimy spróbować później.")
            break


        