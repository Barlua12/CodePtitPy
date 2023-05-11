# Đọc số lượng bộ test T
T = int(input())

# Với mỗi bộ test:
for i in range(T):
    # Đọc số phần tử của mỗi dãy
    N = int(input())

    # Đọc dãy số A và dãy số B
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # Khởi tạo bộ đếm counter cho dãy số B
    counter = {}
    for b in B:
        if b not in counter:
            counter[b] = 0
        counter[b] += 1

    # Kiểm tra xem dãy số A có phải là hoán vị của dãy số B hay không
    is_permutation = True
    for a in A:
        if a not in counter or counter[a] == 0:
            is_permutation = False
            break
        counter[a] -= 1

    # In kết quả của từng bộ test
    if is_permutation:
        print("YES")
    else:
        print("NO")
