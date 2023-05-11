def sum_digits(n):

    return sum(int(digit) for digit in str(n))

n = int(input())
count = 0
if n < 0:
    n = -n
if n<10:
    count=1
while n > 9:
    n = sum_digits(n)
    count +=1

print(count )
