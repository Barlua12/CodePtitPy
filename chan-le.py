def is_valid_number(n):
    digit_sum=sum(int(d) for d in str(n))
    if(digit_sum%10!=0):
        return  False
    
    last_digit=None
    while n>0:
        current_digit=n%10
        if last_digit is not None and abs(current_digit-last_digit)!=2:
            return False
        last_digit=current_digit
        n//=10
    return True

test=int(input())

for i in range(test):
    n=int(input())
    if(is_valid_number(n)):
        print("YES")
    else:
        print("NO")



