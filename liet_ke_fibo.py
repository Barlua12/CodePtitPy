def fib(a, b):
    # Tính toàn bộ dãy Fibonacci từ F1 đến Fk-1
    f = [1, 1]
    i = 2
    while f[i-1] < b:
        f.append(f[i-1] + f[i-2])
        i += 1

    # Lưu trữ các số Fibonacci từ Fj đến Fk-1 vào danh sách
    j = 1
    res = []
    while f[j] < a:
        j += 1
    while f[j] <= b:
        res.append(f[j])
        j += 1

    # In ra danh sách
    print(*res)

# Đọc số bộ test
t = int(input())

# Đọc a và b cho mỗi bộ test và gọi hàm fib để tính và in ra các số Fibonacci từ a đến b
for _ in range(t):
    a, b = map(int, input().split())
    fib(a, b)
