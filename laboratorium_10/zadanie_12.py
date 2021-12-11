def Dictonary_Ascii():
    plik = open("ascii.txt", "r", encoding="utf8") #każdy znak ascii utf8
    line = plik.readline()
    Dict = {}
    while line != "":
        tablica = line.strip().split("=") #strip usuwa białe znaki (tabulacje, spacje, itp) na poczatku i na końcu
        Dict[tablica[1]] = tablica[0]
        line = plik.readline()
    plik.close()
    return Dict

dictonary = Dictonary_Ascii()

n = input("Wprowadź znaki, a otrzymasz kody Ascii: ")

for i in range(len(n)):
    print(n[i], "=", dictonary.get(n[i]))
     