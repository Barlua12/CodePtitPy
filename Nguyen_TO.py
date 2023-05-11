import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def count_coprime(n):
    result = n
    i = 2
    while i * i <= n:
        if n % i == 0:
            while n % i == 0:
                n //= i
            result *= (1 - 1 / i)
        i += 1
    if n > 1:
        result *= (1 - 1 / n)
    return int(result)

t = int(input())
for i in range(t):
    n = int(input())
    k = count_coprime(n)
    if is_prime(k):
        print("YES")
    else:
        print("NO")
