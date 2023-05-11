n, m = map(int, input().split())
A = []
for i in range(n):
    row = list(map(int, input().split()))
    A.append(row)

max_value = max(map(max, A))
min_value = min(map(min, A))
lucky_num = max_value - min_value

positions = []
for i in range(n):
    for j in range(m):
        if A[i][j] == lucky_num:
            positions.append((i, j))

if len(positions) == 0:
    print("NOT FOUND")
else:
    print(lucky_num)
    for pos in positions:
        print("Vi tri [{0}][{1}]".format(pos[0], pos[1]))
