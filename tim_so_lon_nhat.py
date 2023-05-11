t = int(input())

for i in range(t):
    s = input()
    max_num = 0
    temp = 0
    for c in s:
        if c.isdigit():
            temp = temp * 10 + int(c)
            max_num = max(max_num, temp)
        else:
            temp = 0
    print(max_num)
