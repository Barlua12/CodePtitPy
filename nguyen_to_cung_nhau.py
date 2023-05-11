def is_coprime(a, b):
    while b != 0:
        a, b = b, a % b
    return a == 1

N, K = map(int, input().split())

result = []
i = 10 ** (K-1)

while i < 10 ** K:
    if is_coprime(N, i):
        result.append(i)
        if len(result) % 10 == 0:
            print(*result[-10:])
            result = []
    i += 1

if result:
    print(*result)
