n = input()

# Duyệt từ trái sang phải
i = 0
while i < len(n):
    if n[i] == '6':
        # Tìm số 8 hoặc 88 tiếp theo
        j = i + 1
        while j < len(n) and n[j] == '8':
            j += 1
        if j == i + 1:
            # Không tìm thấy số 8
            print('NO')
            exit()
        else:
            # Tìm thấy số 8
            i = j
            # Tiếp tục tìm số 6 hoặc 68 hoặc 688 tiếp theo
            while i < len(n) and n[i] == '6':
                i += 1
            if i == j:
                # Không tìm thấy số 6 hoặc 68 hoặc 688
                print('NO')
                exit()
    else:
        i += 1

# Nếu không có số 6, số đó không phải là số lộc phát đẹp
print('NO')
