#Kalkulator liczb zespolonych

def kalkulator():
    try:
        a1 = int(input("Wprowadź część rzeczywistą pierwszej liczby zespolonej: "))
        b1 = int(input("Wprowadź część urojoną pierwszej liczby zespolonej: "))
        c1 = complex(a1, b1)
        print("Twoja pierwsza liczba zespolona to: ", c1)
        operator = input("Wprowadź operator (+, -, *, /, **): ")
        if operator != "+" and operator != "-" and operator != "*" and operator != "/" and operator != "**":
            print("Nieznany operator!")
            return
        a2 = int(input("Wprowadź część rzeczywistą dugiej liczby zespolonej: "))
        b2 = int(input("Wprowadź część urojoną drugiej liczby zespolonej: "))
        c2 = complex(a2, b2)
        print("Twoja druga liczba zespolona to: ", c2)
        if operator == "+":
            print("Wynik dodawania =", complex((c1.real + c2.real), (c1.imag + c2.imag)))
        elif operator == "-":
            print("Wynik odejmowania =", complex((c1.real - c2.real), (c1.imag - c2.imag)))
        elif operator == "*":
            print("Wynik mnożenia =", complex(((c1.real*c2.real) - (c1.imag*c2.imag)), ((c1.real*c2.imag) + (c2.real*c1.imag))))          
        elif operator == "/":
            if c2.real and c2.imag == 0:
                raise ZeroDivisionError
            else:
                print("Wynik dzielenia =", complex(((c1.real*c2.real + c1.imag*c2.imag)/(c2.real**2 + c2.imag**2)), ((c1.imag*c2.real - c1.real*c2.imag)/(c2.real**2 + c2.imag**2))))
        elif operator == "**":
            if  c1.imag == 0 and c2.imag == 0:
                print("Wynik potęgowania =", c1.real ** c2.real)
            else:
                raise ValueError
    except ValueError:
        print("Wystąpił błąd podczas potęgowania - nieobsługiwana operacja!") 
    except ZeroDivisionError:
        print("Nie dziel przez zero!") 

while True:
    kalkulator()
    loop = input("Czy chcesz skorzystać z kalkulatora jeszcze raz? T/N: ")
    if loop == "N":
        print("Dziękuję za skorzystanie z programu ;)")
        break