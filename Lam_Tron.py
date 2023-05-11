import math

def round_number(n):
    num_digits = math.floor(math.log10(n)) + 1
    if num_digits <= 1:
        return n
    elif num_digits == 2:
        return round(n, -1)
    elif num_digits == 3:
        return round(n, -2)
    elif num_digits == 4:
        return round(n, -3)
    elif num_digits == 5:
        return round(n, -4)
    elif num_digits == 6:
        return round(n, -5)
    elif num_digits == 7:
        return round(n, -6)
    elif num_digits == 8:
        return round(n, -7)
    elif num_digits == 9:
        return round(n, -8)

# Đọc số lượng test case
t = int(input())

# Với mỗi test case
for i in range(t):
    # Đọc số nguyên dương N
    n = int(input())
    # Làm tròn N theo quy tắc đã cho
    n_rounded = round_number(n)
    # In kết quả ra một dòng
    print(n_rounded)
