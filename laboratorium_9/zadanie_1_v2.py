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
        for p in range(len(matrix[0])): #musi być len(matrix[0]), bo bez [0], gdy weźmiemy np. liczbę kolumn > wierszy, to wyprintuje nam pustą ostatnią kolumnę. 
            print(format(matrix[i][p], "<5"), end = " ")
        print() #po każdym wierszu przechodzimy do następnej linii/wiersza

rows = int(input("Podaj liczbę wierszy macierzy: "))
columns = int(input("Podaj liczbę kolumn macierzy: "))

first_matrix = numbers_in_matrix(rows, columns)
print("Twoja pierwsza macierz to:")
printing_matrix(first_matrix)

second_matrix = numbers_in_matrix(rows, columns)
print("Twoja druga macierz to:")
printing_matrix(second_matrix)

sum = [] #macierz z samymi zerami o takich samych wymiarach
for i in range(rows):
    temp = []
    for p in range(columns):
        p = 0
        temp.append(p)
    sum.append(temp)

for i in range(rows):
    for p in range(columns):
        sum[i][p] = first_matrix[i][p] + second_matrix[i][p]

print("Wynik dodawania to:")
for i in range(rows):
    for p in range(columns):
        print(format(sum[i][p], "<5"), end = " ")
    print()

sum = [] #macierz z samymi zerami o takich samych wymiarach
for i in range(rows):
    temp = []
    for p in range(columns):
        p = 0
        temp.append(p)
    sum.append(temp)
 
for i in range(rows):
    for p in range(columns):
        sum[i][p] = first_matrix[i][p] - second_matrix[i][p]

print("Wynik odejmowania to:")
for i in range(rows):
    for p in range(columns):
        print(format(sum[i][p], "<5"), end = " ")
    print()
