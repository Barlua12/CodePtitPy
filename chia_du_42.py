# Nhập dãy số và tính số lượng các số khác nhau khi chia dư cho 42

# Khởi tạo mảng đếm số lượng các số khác nhau
count = [0] * 42

# Nhập dãy số
for i in range(10):
    x = int(input())
    # Tính số dư khi chia cho 42 và tăng giá trị tương ứng trong mảng đếm
    count[x % 42] += 1

# Đếm số lượng phần tử khác 0 trong mảng đếm
result = sum(1 for c in count if c > 0)

# In kết quả
print(result)
