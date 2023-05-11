def count_digits(num):
    # Khởi tạo một mảng đếm tần số xuất hiện của các chữ số từ 0 đến 9
    digit_count = [0] * 10

    # Đếm tần số xuất hiện của các chữ số trong số num
    while num > 0:
        digit = num % 10
        digit_count[digit] += 1
        num //= 10

    # Trả về mảng đếm tần số xuất hiện của các chữ số
    return digit_count


# Đọc số lượng bộ test
T = int(input())

# Với mỗi bộ test
for i in range(T):
    # Đọc 2 số nguyên A và B
    A, B = map(int, input().split())

    # Khởi tạo mảng đếm tần số xuất hiện của các chữ số từ 0 đến 9
    digit_count = [0] * 10

    # Liệt kê tất cả các số từ A đến B
    for num in range(A, B + 1):
        # Đếm tần số xuất hiện của các chữ số trong số num
        num_digit_count = count_digits(num)

        # Cập nhật mảng đếm tần số xuất hiện của các chữ số
        for digit in range(10):
            digit_count[digit] += num_digit_count[digit]

    # In ra tần số xuất hiện của các chữ số
    print(*digit_count)
