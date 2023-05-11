T = int(input())

for i in range(T):
    N = input()
    prod = 1
    for c in N:
        if c != '0':
            prod *= int(c)
    print(prod)
