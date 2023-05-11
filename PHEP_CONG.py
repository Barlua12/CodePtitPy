# Đọc phép toán từ input
operation = input()

# Tách các số a, b, c
a = int(operation[0])
b = int(operation[4])
c = int(operation[8])

# Kiểm tra a + b có bằng c hay không
if a + b == c:
    print("YES")
else:
    print("NO")
