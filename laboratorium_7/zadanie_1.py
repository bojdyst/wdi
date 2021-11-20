#Program zmieniający liczbę na system dwójkowy/ósemkowy/dziesiętny/szesnastkowy 

#Przypadki testowe: 28 na bin; 255 na oct; 14F0 na dec; 100010100011110101111 na hex

system1 = input("W jakim systemie chcesz podać liczbę? Wpisz \"dwójkowy/ósemkowy/dziesiętny/szesnastkowy\": ")
if system1 == "dziesiętny":
    liczba = int(input("Wprowadź liczbę: "))
    system2 = input("Na jaki system chcesz ją zamienić? Wpisz \"dwójkowy/ósemkowy/szesnastkowy\": ")
    
    if system2 == "dwójkowy":
        L = []
        while liczba > 0: #biorę liczbę, sprawdzam jej resztę z dzielenia modulo 2, następnie wpisuje do tablicy. Dzielę liczbę przez 2 (z zaokrągalniem w dół), sprawdzam otrzmaną liczbę modulo 2, wpisuję otrzymaną wartość, itd, aż otrzymana liczba > 0 
            temp = liczba % 2
            liczba = liczba//2
            L.append(temp)        
        L.reverse() #odwracam kolejność cyfr w tablicy, gdyż były zapisywane w niej od lewej do prawej (modulo największej liczby - pierwsza cyfra w tablicy), a my zapisujemy (liczymy) binarnie od prawej.
        print(L)

    elif system2 == "ósemkowy":
        L = []
        while liczba > 0:
            temp = liczba % 8
            liczba = liczba//8
            L.append(temp)
        L.reverse()
        print(L)

    elif system2 == "szesnastkowy":
        L = []
        cyfry = "0123456789ABCDEF"
        while liczba > 0:
            temp = cyfry[liczba % 16] #wybiera liczbę z "cyfry" o numerze kolejności, odpowiadającym reszcie z dzielenia przez 16
            liczba = liczba//16 
            L.append(temp)
        L.reverse()
        print(L)

elif system1 == "dwójkowy":
    liczba = int(input("Wprowadź liczbę: "))
    system2 = input("Na jaki system chcesz ją zamienić? Wpisz \"dziesiętny/ósemkowy/szesnastkowy\": ")
    
    if system2 == "dziesiętny":
        i = 0
        wynik = 0
        while liczba > 0:
            temp = liczba % 10
            wynik = wynik + temp * 2**i
            i = i + 1
            liczba = liczba//10
        print(wynik)

    elif system2 == "ósemkowy":
        i = 0
        wynik = 0
        while liczba > 0:
            temp = liczba % 10
            wynik = wynik + temp * 2**i
            i = i + 1
            liczba = liczba//10
        bool(wynik) 
        L = []
        while wynik > 0:
            temp = wynik % 8
            wynik = wynik//8
            L.append(temp)
        L.reverse()
        print(L)

    elif system2 == "szesnastkowy":
        i = 0
        wynik = 0
        while liczba > 0:
            temp = liczba % 10
            wynik = wynik + temp * 2**i
            i = i + 1
            liczba = liczba//10
        bool(wynik) 
        L = []
        cyfry = "0123456789ABCDEF"
        while wynik > 0:
            temp = cyfry[wynik % 16]
            wynik = wynik//16
            L.append(temp)
        L.reverse()
        print(L)

elif system1 == "ósemkowy":
    liczba = int(input("Wprowadź liczbę: "))
    system2 = input("Na jaki system chcesz ją zamienić? Wpisz \"dwójkowy/dziesiętny/szesnastkowy\": ")

    if system2 == "dwójkowy":
        wynik = 0
        i = 0
        while liczba > 0:
            temp = liczba % 10
            wynik = wynik + temp * 8**i
            i = i + 1 
            liczba = liczba//10
        bool(wynik)
        L = []
        while wynik > 0: 
            temp = wynik % 2
            wynik = wynik//2
            L.append(temp)        
        L.reverse() 
        print(L)

    elif system2 == "dziesiętny":
        wynik = 0
        i = 0
        while liczba > 0:
            temp = liczba % 10
            wynik = wynik + temp * 8**i
            i = i + 1 
            liczba = liczba//10
        print(wynik)

    elif system2 == "szesnastkowy":
        wynik = 0
        i = 0
        while liczba > 0:
            temp = liczba % 10
            wynik = wynik + temp * 8**i
            i = i + 1 
            liczba = liczba//10
        bool(wynik)
        L = []
        cyfry = "0123456789ABCDEF"
        while wynik > 0:
            temp = cyfry[wynik % 16] 
            wynik = wynik//16 
            L.append(temp)
        L.reverse()
        print(L)

elif system1 == "szesnastkowy":
    liczba = list(input("Wprowadź liczbę: "))
    system2 = input("Na jaki system chcesz ją zamienić? Wpisz \"dwójkowy/ósemkowy/dziesiętny\": ")

    if system2 == "dziesiętny":
        dlugosc = len(liczba)
        wynik = 0
        for i in range(dlugosc):
            ostatni = liczba.pop()
            if ostatni == "0":
                wynik = wynik + (16**i)*0
            elif ostatni == "1":
                wynik = wynik + (16**i)*1
            elif ostatni == "2":
                wynik = wynik + (16**i)*2
            elif ostatni == "3":
                wynik = wynik + (16**i)*3
            elif ostatni == "4":
                wynik = wynik + (16**i)*4
            elif ostatni == "5":
                wynik = wynik + (16**i)*5
            elif ostatni == "6":
                wynik = wynik + (16**i)*6
            elif ostatni == "7":
                wynik = wynik + (16**i)*7
            elif ostatni == "8":
                wynik = wynik + (16**i)*8
            elif ostatni == "9":
                wynik = wynik + (16**i)*9
            elif ostatni == "A":
                wynik = wynik + (16**i)*10
            elif ostatni == "B":
                wynik = wynik + (16**i)*11
            elif ostatni == "C":
                wynik = wynik + (16**i)*12
            elif ostatni == "D":
                wynik = wynik + (16**i)*13
            elif ostatni == "E":
                wynik = wynik + (16**i)*14
            elif ostatni == "F":
                wynik = wynik + (16**i)*15
        print(wynik)

    elif system2 == "dwójkowy":
        dlugosc = len(liczba)
        wynik = 0
        for i in range(dlugosc):
            ostatni = liczba.pop()
            if ostatni == "0":
                wynik = wynik + (16**i)*0
            elif ostatni == "1":
                wynik = wynik + (16**i)*1
            elif ostatni == "2":
                wynik = wynik + (16**i)*2
            elif ostatni == "3":
                wynik = wynik + (16**i)*3
            elif ostatni == "4":
                wynik = wynik + (16**i)*4
            elif ostatni == "5":
                wynik = wynik + (16**i)*5
            elif ostatni == "6":
                wynik = wynik + (16**i)*6
            elif ostatni == "7":
                wynik = wynik + (16**i)*7
            elif ostatni == "8":
                wynik = wynik + (16**i)*8
            elif ostatni == "9":
                wynik = wynik + (16**i)*9
            elif ostatni == "A":
                wynik = wynik + (16**i)*10
            elif ostatni == "B":
                wynik = wynik + (16**i)*11
            elif ostatni == "C":
                wynik = wynik + (16**i)*12
            elif ostatni == "D":
                wynik = wynik + (16**i)*13
            elif ostatni == "E":
                wynik = wynik + (16**i)*14
            elif ostatni == "F":
                wynik = wynik + (16**i)*15
        bool(wynik)
        L = []
        while wynik > 0: 
            temp = wynik % 2
            wynik = wynik//2
            L.append(temp)        
        L.reverse() 
        print(L)

    elif system2 == "ósemkowy":
        dlugosc = len(liczba)
        wynik = 0
        for i in range(dlugosc):
            ostatni = liczba.pop()
            if ostatni == "0":
                wynik = wynik + (16**i)*0
            elif ostatni == "1":
                wynik = wynik + (16**i)*1
            elif ostatni == "2":
                wynik = wynik + (16**i)*2
            elif ostatni == "3":
                wynik = wynik + (16**i)*3
            elif ostatni == "4":
                wynik = wynik + (16**i)*4
            elif ostatni == "5":
                wynik = wynik + (16**i)*5
            elif ostatni == "6":
                wynik = wynik + (16**i)*6
            elif ostatni == "7":
                wynik = wynik + (16**i)*7
            elif ostatni == "8":
                wynik = wynik + (16**i)*8
            elif ostatni == "9":
                wynik = wynik + (16**i)*9
            elif ostatni == "A":
                wynik = wynik + (16**i)*10
            elif ostatni == "B":
                wynik = wynik + (16**i)*11
            elif ostatni == "C":
                wynik = wynik + (16**i)*12
            elif ostatni == "D":
                wynik = wynik + (16**i)*13
            elif ostatni == "E":
                wynik = wynik + (16**i)*14
            elif ostatni == "F":
                wynik = wynik + (16**i)*15
        bool(wynik) 
        L = []
        while wynik > 0:
            temp = wynik % 8
            wynik = wynik//8
            L.append(temp)
        L.reverse()
        print(L)