t = int(input())

for i in range(t):
    s = input().strip()
    max_num = ""
    current_num = ""

    for c in s:
        if c.isdigit():
            current_num += c
        else:
            if current_num != "":
                if current_num > max_num:
                    max_num = current_num
                current_num = ""

    if current_num != "" and current_num > max_num:
        max_num = current_num

    print(max_num)
