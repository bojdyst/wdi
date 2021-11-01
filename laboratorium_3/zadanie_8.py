height = int(input("Wprowadź liczbę całkowitą, nieujemną "))

for a in range(height):
    print((" " * (height - a)) + ("*" * ((2 * a) + 1)))
 
print((" " * height) + "U")
 