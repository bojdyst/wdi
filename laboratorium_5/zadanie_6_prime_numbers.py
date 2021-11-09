#Sprawdź, czy zadana liczba jest liczbą pierwszą

def czy_jest_pierwszą():
    liczba = int(input("Wprowadź liczbę i sprawdź, czy jest liczbą pierwszą!: "))
    if liczba < 2:
        print("Liczba", liczba, "NIE jest liczbą pierwszą!")
    elif liczba == 2:
        print("Liczba", liczba, "jest liczbą pierwszą!")
    elif liczba > 2:
        for i in range(3, liczba, 2):
            if liczba % i == 0:
                print("Liczba", liczba, "NIE jest liczbą pierwszą!")
                return
        print("Liczba", liczba, "jest liczbą pierwszą!")

while True: 
    czy_jest_pierwszą()
    loop = input("Czy chesz wprowadzić kolejną liczbę? Wpisz T/N: ")
    if loop == "N":
        print("Dziękuję za skorzystanie z programu! Miłego dnia ;)")
        break  


