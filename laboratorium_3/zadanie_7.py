from statistics import median
a = int(input("Podaj pierwszą liczbę "))
b = int(input("Podaj drugą liczbę "))

middle = int(median(range(a,b)))

for number in range(a,b):
    if len(range(a,b)) <=20:
        print(number)
if len(range(a,b)) >20:
    print(middle - 3, middle - 2, middle - 1, middle +1, middle + 2, middle +3)
