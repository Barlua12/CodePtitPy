def is_tang_giam(n):
    digits = [int(d) for d in str(n)]  # chuyển số n thành một danh sách các chữ số
    n_digits = len(digits)
    if n_digits<3:
        return False
    i = 1
    while i < n_digits and digits[i] >= digits[i-1]:  # tìm vị trí đầu tiên mà chữ số tại vị trí đó bé hơn chữ số trước đó
        i += 1
    if i == n_digits:  # nếu không tìm được vị trí thích hợp thì không phải số tăng giảm
        return False
    while i < n_digits and digits[i] <= digits[i-1]:  # kiểm tra xem các chữ số từ vị trí tìm được trở đi có giảm chặt không
        i += 1
    return True  # nếu hết danh sách rồi mà không thoả điều kiện thì đó là số tăng giảm

n_tests = int(input())
for i in range(n_tests):
    n = int(input())
    if is_tang_giam(n):
        print("YES")
    else:
        print("NO")
