def encode(s):
    res = ''
    i = 0
    while i < len(s):
        j = i
        while j < len(s) and s[j] == s[i]:
            j += 1
        res += s[i] + str(j - i)
        i = j
    return res


def decode(s):
    res = ''
    i = 0
    while i < len(s):
        if s[i].isalpha():
            res += s[i]
            j = i + 1
            while j < len(s) and s[j].isdigit():
                j += 1
            count = int(s[i + 1:j])
            res += s[i] * count
            i = j
        else:
            i += 1
    return res


# Đọc số bộ test
t = int(input())

# Duyệt qua các bộ test
for i in range(t):
    # Đọc xâu kết quả mã hóa
    s = input()

    # Giải mã xâu kết quả và in ra kết quả
    print(decode(s))
