def reverse_number(n):
    """Trả về số đảo ngược của số n"""
    return int(str(n)[::-1])


def find_multiple_of_seven(n):
    """Tìm giá trị chia hết cho 7 đầu tiên tìm được sau các bước tính tổng"""
    count = 0
    while count < 1000:
        if n % 7 == 0:
            return n
        n += reverse_number(n)
        count += 1
    return -1


t = int(input())
for _ in range(t):
    n = int(input())
    print(find_multiple_of_seven(n))
