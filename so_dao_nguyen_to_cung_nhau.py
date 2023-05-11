import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def reverse_number(n):
    return int(str(n)[::-1])

t = int(input())
for _ in range(t):
    n = int(input())
    reverse_n = reverse_number(n)
    if math.gcd(n, reverse_n) == 1:
        print("YES")
    else:
        print("NO")
