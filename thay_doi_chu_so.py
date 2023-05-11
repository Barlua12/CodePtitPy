def get_sum(s1, s2):
    return str(int(s1) + int(s2))

def get_min_sum(X1, X2):
    p, q = map(str, input().split())
    X1 = X1.replace(p, q)
    X2 = X2.replace(p, q)
    X1_sorted = ''.join(sorted(X1))
    X2_sorted = ''.join(sorted(X2))
    X1_sum = int(X1_sorted)
    X2_sum = int(X2_sorted)
    return get_sum(str(X1_sum), str(X2_sum))

def get_max_sum(X1, X2):
    p, q = map(str, input().split())
    X1 = X1.replace(p, q)
    X2 = X2.replace(p, q)
    X1_sorted = ''.join(sorted(X1, reverse=True))
    X2_sorted = ''.join(sorted(X2, reverse=True))
    X1_sum = int(X1_sorted)
    X2_sum = int(X2_sorted)
    return get_sum(str(X1_sum), str(X2_sum))

# main
T = int(input())
for i in range(T):
    X1 = input().strip()
    X2 = input().strip()
    print(get_min_sum(X1, X2), get_max_sum(X1, X2))
