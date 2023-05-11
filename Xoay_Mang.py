def rotate_array(A, d):
    # Tạo mảng temp gồm d phần tử đầu tiên của mảng A
    temp = A[:d]

    # Dịch chuyển mảng A sang trái d phần tử
    for i in range(d, len(A)):
        A[i - d] = A[i]

    # Gán các phần tử trong mảng temp vào cuối mảng A
    for i in range(len(temp)):
        A[len(A) - d + i] = temp[i]

    return A


# Đọc input
T = int(input())
for t in range(T):
    N, d = map(int, input().split())
    A = list(map(int, input().split()))

    # Thực hiện quay mảng A
    A = rotate_array(A, d)

    # In kết quả
    print(*A)
