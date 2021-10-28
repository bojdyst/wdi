a = int(input("Wprowadź pierwszą liczbę "))
b = int(input("Wprowadź drugą liczbę "))

def function_multiplication():
    print("Wynik dodawania", a+b) 
    print("Wynik odejmowania",a-b) 
    print("Wynik mnożenia", a*b)    
    print("Wynik dzielenia", a/b) 
    print("Wynik kwadratowania", "Pierwsza liczba", a**2, "Druga liczba", b**2)
    print("Wynik pierwiastkowania", "Pierwsza liczba", a**(1/2), "Druga liczba", b**(1/2))

def function_print():
    if a*b==10:
        function_multiplication()
        print("Wynik mnożenia to 10, Yay!")
    else: 
        function_multiplication()

if a<0 and b<0:
    print("Obie liczby są mniejsze od 0 - program zostanie zakończony")
    pass 
elif (a>0) and (b<0):
    b = b * (-1)
    function_print()
elif (a<0) and (b>0):
    a = a * (-1)
    function_print()
else:
    function_print()