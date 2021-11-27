from random import randint

def Is_prime_number(a):
    for j in range(3, a):
        if a % j == 0:  
            return False
    return True

def Prime():
    P = [2]
    for i in range(3, 100, 2):
        if Is_prime_number(i) == True:
            P.append(i)
    return P       

N = int(input("Podaj liczbę N, z jakiej ma składać się lista: "))
L = []
for p in range(N):
    L.append(randint(1,100))
print("Twoja wygenerowana lista to:", L)

Prime_numbers = Prime()
for i in range(len(Prime_numbers)):
    try:
        index = L.index(Prime_numbers[i]) #zwraca numer indeksu pierwszej liczby pierwszej w L
        while True:
            L.insert(index + 1, 0)
            index = L.index(Prime_numbers[i], index + 1) #szukamy kolejnej liczby pierwszej, startujemy od liczby "index + 1", aby uniknąć szukania od już znalezionej liczby pierwszej
    except:
        continue

print("Twoja lista uzupełniona o zera to:", L)

sum = 0 
last_zero = 0
for p in range(len(L)):
    if L[p] != 0:
        sum += L[p]
    elif L[p] == 0:
        print(L[last_zero : p], sum)
        last_zero = p + 1
        sum = 0
if sum != 0:
    print(L[last_zero : len(L)], sum)      





