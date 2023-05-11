t = int(input())

for _ in range(t):
    s = input()
    min_num = None
    curr_num = ''
    for c in s:
        if c.isdigit():
            curr_num += c
        else:
            if curr_num:
                num = int(curr_num)
                if min_num is None or num < min_num:
                    min_num = num
                curr_num = ''
    if curr_num:
        num = int(curr_num)
        if min_num is None or num < min_num:
            min_num = num
    print(min_num)
