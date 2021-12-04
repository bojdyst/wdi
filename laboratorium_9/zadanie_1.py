def numbers_in_matrix(m,n):
    matrix = []
    for i in range(m):
        temp = []
        for p in range(n):
            p = int(input("Podaj liczbę do macierzy: ["+str(i)+"]  ["+str(p)+"] "))
            temp.append(p)
        matrix.append(temp)
    return matrix

def printing_matrix(matrix):
    for i in range(len(matrix)):
        for p in range(len(matrix[0])):
            print(format(matrix[i][p], "<5"), end = " ")
        print() #po każdym wierszu przechodzimy do następnej linii

rows_1 = int(input("Podaj liczbę wierszy pierwszej macierzy: "))
columns_1 = int(input("Podaj liczbę kolumn pierwszej macierzy: "))

first_matrix = numbers_in_matrix(rows_1, columns_1)
print("Twoja pierwsza macierz to:")
printing_matrix(first_matrix)

try:
    rows_2 = int(input("Podaj liczbę wierszy drugiej macierzy: "))
    columns_2 = int(input("Podaj liczbę kolumn drugiej macierzy: "))
    if rows_2 != rows_1 or columns_2 != columns_1:
        raise ValueError
    else:
        second_matrix = numbers_in_matrix(rows_2, columns_2)
        print("Twoja druga macierz to:")
        printing_matrix(second_matrix)
except ValueError:
        print("Działania możemy wykonywać tylko na macierzach tego samego wymiaru!")

sum = []
for i in range(rows_1):
    temp = []
    for p in range(columns_1):
        p = 0
        temp.append(p)
    sum.append(temp)

for i in range(rows_1):
    for p in range(columns_1):
        sum[i][p] = first_matrix[i][p] + second_matrix[i][p]

print("Wynik dodawania to:")
for i in range(rows_1):
    for p in range(columns_1):
        print(format(sum[i][p], "<5"), end = " ")
    print()

sum = []
for i in range(rows_1):
    temp = []
    for p in range(columns_1):
        p = 0
        temp.append(p)
    sum.append(temp)

for i in range(rows_1):
    for p in range(columns_1):
        sum[i][p] = first_matrix[i][p] - second_matrix[i][p]

print("Wynik odejmowania to:")
for i in range(rows_1):
    for p in range(columns_1):
        print(format(sum[i][p], "<5"), end = " ")
    print()
