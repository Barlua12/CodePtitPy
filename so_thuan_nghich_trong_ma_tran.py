def is_palindrome(num):
    """
    Kiểm tra xem một số có phải là số thuận nghịch hay không.
    """
    str_num = str(num)
    return str_num == str_num[::-1] and len(str_num) > 1

n, m = map(int, input().split())

# Tìm số thuận nghịch lớn nhất trong ma trận
max_palindrome = None
max_palindrome_positions = []
for i in range(n):
    row = list(map(int, input().split()))
    for j, num in enumerate(row):
        if is_palindrome(num) and (max_palindrome is None or num > max_palindrome):
            max_palindrome = num
            max_palindrome_positions = [(i, j)]
        elif is_palindrome(num) and num == max_palindrome:
            max_palindrome_positions.append((i, j))

# In kết quả
if max_palindrome is None:
    print("NOT FOUND")
else:
    print(max_palindrome)
    for i, j in max_palindrome_positions:
        print(f"Vi tri [{i}][{j}]")
