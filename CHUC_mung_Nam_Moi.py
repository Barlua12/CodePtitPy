n = int(input())
count_map = {}
unique_set = set()
for i in range(n):
    s = input().strip().replace(" ", "")
    if s in count_map:
        count_map[s] += 1
    else:
        count_map[s] = 1
        unique_set.add(s)
print(len(unique_set))
