s1 = input()
s2 = input()
p = int(input())

result = s1[:p] + s2 + s1[p:]
print(result)