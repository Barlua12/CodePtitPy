def is_non_decreasing(num):
    for i in range(len(num)-1):
        if num[i] > num[i+1]:
            return "NO"
    return "YES"

# Đọc số bộ test
t = int(input())

# Duyệt qua từng bộ test và kiểm tra từng số
for _ in range(t):
    num = input().strip()
    print(is_non_decreasing(num))
