def generate_palindromes(length, prefix, palindromes):
    if length == 0:
        palindromes.append(int(prefix))
        return
    for digit in ['0', '2', '4', '6', '8']:
        new_prefix = digit + prefix + digit
        generate_palindromes(length - 2, new_prefix, palindromes)

def list_palindromes_less_than_n(n):
    palindromes = []
    for length in range(1, n):
        if length % 2 == 0:
            continue
        generate_palindromes(length, '', palindromes)
    result = []
    for p in palindromes:
        if p < n:
            result.append(p)
    return result

# Đọc số bộ test
t = int(input())

for i in range(t):
    n = int(input())
    palindromes = list_palindromes_less_than_n(n)
    print(*palindromes)
