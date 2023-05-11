n = int(input())
a = list(map(int, input().split()))

count = 0
for i in range(1, n):
    for j in range(i):
        if a[j] > a[i]:
            count += 1

print(count)
