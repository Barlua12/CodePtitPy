def shrink_array(A):
    while True:
        found = False
        for i in range(0, len(A)-1):
            if (A[i] + A[i+1]) % 2 == 0:
                del A[i:i+2]
                found = True
                break
        if not found:
            return len(A)

n = int(input())
A = list(map(int, input().split()))
print(shrink_array(A))