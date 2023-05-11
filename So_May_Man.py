def count_lucky_digits(n):
    count_4=0
    count_7=0
    for digit in str(n):
        if digit=='4':
            count_4+=1
        if digit=='7':
            count_7+=1
    if (count_7+count_4 == 4 or count_7+count_4 == 7):
        print("YES")
    else:
        print("NO")

number_test=int(input())

for i in range(number_test):
    n=int(input())
    count_lucky_digits(n)