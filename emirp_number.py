def is_prime(n):
    """Kiểm tra n có phải số nguyên tố không."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def reverse_string(s):
    """Đảo ngược chuỗi s."""
    return s[::-1]


def is_emirp(n):
    """Kiểm tra n có phải là số Emirp hay không."""
    if not is_prime(n):
        return False
    reverse_n = int(reverse_string(str(n)))
    return n != reverse_n and is_prime(reverse_n)


# Đọc số lượng bộ test
t = int(input())

# Duyệt qua các bộ test
for _ in range(t):
    n = int(input())
    emirps = [str(x) for x in range(13, n) if is_emirp(x)]
    print(" ".join(emirps))
