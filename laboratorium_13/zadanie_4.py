import time

N = int(input("Wprawadź N-tą liczbę ciągu Fibonacciego: "))

def iterative_fib(n):
    a = 0
    b = 1
    tab = [0,1]
    for i in range(n - 1):
        number = a + b
        tab.append(number)
        a, b = b, a + b
    return tab[n]

start = time.time()

print(iterative_fib(N))

print("iterative:", time.time() - start)

def recursively_fib(n):
    if n == 0: 
        return 0
    elif n == 1: 
        return 1
    else:
        return recursively_fib(n - 1) + recursively_fib(n - 2)

start_2 = time.time()

print(recursively_fib(N))

print("recurisevly:", time.time() - start_2)

def recursively_dict_fib(n):
    if n == 0: 
        return 0
    elif n == 1: 
        return 1
    else:
        return recursively_fib(n - 1) + recursively_fib(n - 2)