def is_beautiful_number(n):
    n_str=str(n);
    if len(set(n_str))!=2:
        return False
    for i in range(len(n_str)-2):
        if n_str[i]!=n_str[i+2]:
            return False
    return True

test=int(input())
for i in range(test):
    n=int(input())
    if(is_beautiful_number(n)):
        print("YES")
    else:
        print("NO")