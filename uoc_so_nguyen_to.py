def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def digit_sum(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    d = gcd(a, b)
    sum = digit_sum(d)
    if is_prime(sum):
        print("YES")
    else:
        print("NO")
