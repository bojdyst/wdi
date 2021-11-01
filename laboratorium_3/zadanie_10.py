import random



firstoffall = input("Czy chcesz losować liczbę, czy użyć kalkulatora? Wpisz Kalkulator lub Generator ")

if firstoffall == "Kalkulator":
        liczba1 = float(input("Wprowadź pierwszą liczbę "))
        operator = input("Wprowadź operator (+, -, *, /, **, ^) ")
        if operator == "**":
                print("WYNIK: ", liczba1 ** (1/2))
        else:
                liczba2 = float(input("Wprowadź drugą liczbę "))

                if operator == "+":
                        print("WYNIK: ", liczba1 + liczba2)
                elif operator == "-":
                       print("WYNIK: ", liczba1 - liczba2)
                elif operator == "*":
                        print("WYNIK: ", liczba1 * liczba2)
                elif operator == "/":
                        print("WYNIK: ", liczba1 / liczba2)
                elif operator == "^":
                        print("WYNIK: ", liczba1 ** liczba2)
                else:
                        print("Nieznany operator")

if firstoffall == "Generator":
    c = input("Wciśnij x ")
    print(random.uniform(-1000000, 1000000))
 
powtorka = input("Czy chcesz wprowadzić nowe dane? Wpisz T lub N ")
while powtorka == "T":
        firstoffall = input("Czy chcesz losować liczbę, czy użyć kalkulatora? Wpisz Kalkulator lub Generator ")

        if firstoffall == "Kalkulator":
                liczba1 = float(input("Wprowadź pierwszą liczbę "))
                operator = input("Wprowadź operator (+, -, *, /, **, ^) ")
                if operator == "**":
                        print("WYNIK: ", liczba1 ** (1/2))
                else:
                        liczba2 = float(input("Wprowadź drugą liczbę "))

                        if operator == "+":
                                print("WYNIK: ", liczba1 + liczba2)
                        elif operator == "-":
                                print("WYNIK: ", liczba1 - liczba2)
                        elif operator == "*":
                                print("WYNIK: ", liczba1 * liczba2)
                        elif operator == "/":
                                print("WYNIK: ", liczba1 / liczba2)
                        elif operator == "^":
                                print("WYNIK: ", liczba1 ** liczba2)
                        else:
                                print("Nieznany operator")

        if firstoffall == "Generator":
                c = input("Wciśnij x ")
                print(random.uniform(-1000000, 1000000))
        
        powtorka = input("Czy chcesz wprowadzić nowe dane? Wpisz T lub N ")
        
else:
        print("Dziękuję")
    