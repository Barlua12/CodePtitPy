t = int(input())

def check(t):
    number_digits=len(str(t))
    first_number = t // 10**(number_digits-2)
    last_number=   t%100
    if(first_number==last_number):
        return  "YES"
    else:
        return "NO"

for i in range(t):
    n=int(input())
    print(check(n))