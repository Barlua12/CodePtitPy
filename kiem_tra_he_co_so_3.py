t = int(input())

for i in range(t):
    s = input()
    valid = True
    for c in s:
        if c not in ['0', '1', '2']:
            valid = False
            break
    if valid:
        print("YES")
    else:
        print("NO")
