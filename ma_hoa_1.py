T = int(input())

for t in range(T):
    s = input().strip()

    # Khởi tạo biến đếm ban đầu và ký tự trước đó
    count = 1
    prev = s[0]

    # Duyệt từ ký tự thứ hai trở đi
    for i in range(1, len(s)):
        if s[i] == prev:
            # Nếu ký tự hiện tại giống với ký tự trước đó, tăng biến đếm
            count += 1
        else:
            # Ngược lại, in ra biến đếm và ký tự trước đó
            print(str(count) + prev, end="")
            count = 1
            prev = s[i]

    # In ra ký tự cuối cùng và biến đếm tương ứng
    print(str(count) + prev)
