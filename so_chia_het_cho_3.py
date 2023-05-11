def is_divisible_by_3(n):
    sum_digits=sum(int(d) for d in str(n))
    if(sum_digits%3==0):
        return True
    else:
        return False

t=int(input())
for i in range(t):
    n=int(input())
    if(is_divisible_by_3(n)):
        print("YES")
    else:
        print("NO")