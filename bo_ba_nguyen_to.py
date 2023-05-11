def is_coprime(a,b):
    while b!=0:
        a,b=b,a%b
    return a==1

L, R = map(int, input().split())

for i in range(L, R - 1):
    for j in range(i + 1, R):
        for k in range(j + 1, R + 1):
            if is_coprime(i, j) and is_coprime(j, k) and is_coprime(i, k):
                print(f'({i}, {j}, {k})')