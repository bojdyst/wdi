#Sprawdź, czy zadana liczba jest liczbą pierwszą

def czy_jest_pierwszą(n):
    if type(n) not in [int, float]:
        raise TypeError("Podaj liczbę, nie słowo!")
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False
    for dzielnik in range(3, n, 2):
        if n % dzielnik == 0:
            return False
    return True


# while True: 
#     czy_jest_pierwszą()
#     loop = input("Czy chesz wprowadzić kolejną liczbę? Wpisz T/N: ")
#     if loop == "N":
#         print("Dziękuję za skorzystanie z programu! Miłego dnia ;)")
#         break  


