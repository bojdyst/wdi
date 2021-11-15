#Kalkulator liczb zespolonych

def kalkulator():
    z1 = complex(input("Wprowadź pierwszą liczbę zespoloną (w postaci a+bj): "))
    operator = input("Wprowadź operator (+, -, *, /, **): ")
    if operator != "+" and operator != "-" and operator != "*" and operator != "/" and operator != "**":
        print("Nieznany operator!")
        return
    z2 = complex(input("Wprowadź drugą liczbę zespoloną (w postaci: a+bj): " ))
    if operator == "+":
        print("Wynik dodawania =", z1 + z2)
    elif operator == "-":
        print("Wynik odejmowania =", z1 - z2)
    elif operator == "*":
        print("Wynik mnożenia =", z1 * z2)
    elif operator == "/":
        print("Wynik dzielenia =", z1 / z2)
    elif operator == "**":
        if z2.imag == 0:
            print("Wynik potęgowania =", z1 ** z2)
        else:
            print("Wystąpił błąd podczas potęgowania - nieobsługiwana operacja!")
        
while True:
    kalkulator()
    loop = input("Czy chcesz skorzystać z kalkulatora jeszcze raz? T/N: ")
    if loop == "N":
        print("Dziękuję za skorzystanie z programu ;)")
        break
