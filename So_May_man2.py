def is_lucky_number(n):
    for digit in str(n):
        if digit != '4' and digit != '7':
            return "NO"
    return "YES"

number_test=int(input())

for i in range(number_test):
    n=int(input())
    print(is_lucky_number(n))
