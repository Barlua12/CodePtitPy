def find_min_sum(arr, n):
    # Khởi tạo tổng nhỏ nhất là một giá trị lớn
    min_sum = float('inf')

    # Duyệt qua từng phần tử trong mảng
    for i in range(n):
        # Cố định phần tử đầu tiên trong bộ ba
        first = arr[i]

        # Tìm hai phần tử khác trong mảng sao cho tổng của bộ ba là nhỏ nhất
        for j in range(i + 1, n):
            second = arr[j]
            for k in range(j + 1, n):
                third = arr[k]

                # Tính tổng của bộ ba số này
                triplet_sum = first + second + third

                # Nếu tổng của bộ ba này nhỏ hơn tổng nhỏ nhất hiện tại
                # thì cập nhật tổng nhỏ nhất
                if triplet_sum < min_sum:
                    min_sum = triplet_sum

    # Trả về tổng nhỏ nhất của bộ ba số
    return min_sum

# Đọc số lượng bộ test
t = int(input())

for i in range(t):
    # Đọc số lượng phần tử của mảng và các phần tử trong mảng
    n = int(input())
    arr = list(map(int, input().split()))

    # Tìm tổng nhỏ nhất của bộ ba số trong mảng
    min_sum = find_min_sum(arr, n)

    # In ra kết quả
    print(min_sum)
