#Sprawdź, czy zadana liczba jest liczbą pierwszą

while True:
    liczba = int(input("Wprowadź liczbę i sprawdź, czy jest liczbą pierwszą!: "))
    if liczba < 2:
        print("Liczba", liczba, "NIE jest liczbą pierwszą!")
    elif liczba == 2:
        print("Liczba", liczba, "jest liczbą pierwszą!")
    elif liczba > 2:
        for i in range(2, liczba):
            if liczba % i == 0:
                print("Liczba", liczba, "NIE jest liczbą pierwszą!")
                break
            else: 
                print("Liczba", liczba, "jest liczbą pierwszą!")
                break
    loop = input("Czy chesz wprowadzić kolejną liczbę? Wpisz T/N: ")
    if loop == "N":
        print("Dziękuję za skorzystanie z programu! Miłego dnia ;)")
        break  
    if loop == "T":
        liczba = int(input("Wprowadź liczbę i sprawdź, czy jest liczbą pierwszą!: "))
        if liczba < 2:
            print("Liczba", liczba, "NIE jest liczbą pierwszą!")
        elif liczba == 2:
            print("Liczba", liczba, "jest liczbą pierwszą!")
        elif liczba > 2:
            for i in range(2, liczba):
                if liczba % i == 0:
                    print("Liczba", liczba, "NIE jest liczbą pierwszą!")
                    break
                else: 
                    print("Liczba", liczba, "jest liczbą pierwszą!")
                    break
        loop = input("Czy chesz wprowadzić kolejną liczbę? Wpisz T/N: ")
        if loop == "N":
            print("Dziękuję za skorzystanie z programu! Miłego dnia ;)")
            break  
    else:
        print("Nie wybrałeś T - program zostanie zakończony.")
        break