t = int(input())
for i in range(t):
    a, K, N = map(int, input().split())
    min_b = K * (a // K + 1) - a
    found = False
    for b in range(min_b, N - a + 1, K):
        if (a + b) % K == 0:
            print(b, end=' ')
            found = True
    if not found:
        print(-1)
    else:
        print()
