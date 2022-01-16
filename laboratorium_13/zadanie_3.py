import time

# M = int(input("Wprowadź liczbę: "))
# N = int(input("Wprowadź potęgę: "))

def potegowanie(m,n):
    if n == 0:
        return 1
    else: 
        return m * potegowanie(m, n - 1)

def is_prime_rec(a, b = 2):
    if a == b:
        return 1
    if a % b == 0:
        return 0
    return is_prime_rec(a, b + 1)

# if is_prime_rec(N) == 1:
#     time.sleep(M)

# print(potegowanie(M,N))
# print(is_prime_rec(N))