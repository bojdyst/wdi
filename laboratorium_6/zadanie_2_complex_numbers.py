#Wykonaj działania na liczbach zespolonych już dziś!
z1 = complex(input("Wprowadź pierwszą liczbę zespoloną (w postaci a+bj): "))
z2 = complex(input("Wprowadź drugą liczbę zespoloną (w postaci: a+bj): " ))

#dodawanie
sum = print("Wynik dodawania =", z1 + z2)

#odejmowanie
difference = print("Wynik odejmowania =", z1 - z2)

#mnożenie
multiplication = print("Wynik mnożenia =", z1 * z2)

#dzielenie 
try:
    if z2 == 0:
        raise ZeroDivisionError
    else:
        division = print("Wynik dzielenia =", z1 / z2)
except ZeroDivisionError:
    print("Nie dziel przez zero!")    

#potęgowanie
try:
    if z2.imag == 0:
        exponentiation = print("Wynik potęgowania =", z1 ** z2)
    else:
        raise ValueError("Wystąpił błąd podczas potęgowania - nieobsługiwana operacja!")
except ValueError:
    print("Wystąpił błąd podczas potęgowania - nieobsługiwana operacja!") 