# #Binary to decimal

# liczba = int(input("Wprowadź liczbę w systemie dwójkowym: "))
# i = 0
# wynik = 0
# while liczba > 0:
#     temp = liczba % 10
#     wynik = wynik + temp * 2**i
#     i = i + 1
#     liczba = liczba//10
# print(wynik)

#Octal to decimal
# liczba = int(input("Wprowadź liczbę w systemie ósemkowym: "))
# wynik = 0
# i = 0
# while liczba > 0:
#     temp = liczba % 10
#     wynik = wynik + temp * 8**i
#     i = i + 1 
#     liczba = liczba//10
# print(wynik)

#Hexadecimal to decimal
liczba = list(input("Wprowadź liczbę w systemie szesnastkowym: "))
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


# cyfry = "0123456789ABCDEF"
# wynik = 0
# i = 0
# while liczba > 0:
#     temp = cyfry[liczba % 16]
#     wynik = wynik + temp * 16**i
#     i = i + 1 
#     liczba = liczba//16
# print(wynik)

# L = []
#         cyfry = "0123456789ABCDEF"
#         while liczba > 0:
#             temp = cyfry[liczba % 16] #wybiera liczbę z "cyfry" o numerze kolejności, odpowiadającym reszcie z dzielenia przez 16
#             liczba = liczba//16 
#             L.append(temp)
#         L.reverse()
#         print(L)