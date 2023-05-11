t = int(input())

for _ in range(t):
    s = input().strip()
    s_reverse = s[::-1]
    is_balanced = True
    for i in range(1, len(s)):
        if abs(ord(s[i]) - ord(s[i-1])) != abs(ord(s_reverse[i]) - ord(s_reverse[i-1])):
            is_balanced = False
            break
    if is_balanced:
        print("YES")
    else:
        print("NO")
