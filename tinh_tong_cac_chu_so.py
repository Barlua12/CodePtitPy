t = int(input())

for _ in range(t):
    s = input()
    letters = []
    digits_sum = 0

    for char in sorted(s):
        if char.isalpha():
            letters.append(char)
        elif char.isdigit():
            digits_sum += int(char)

    print(''.join(letters) + str(digits_sum))
