def insert_comma(n):
    n_str=str(n)
    n_length=len(n_str)

    first_group_length=n_length%3

    groups=[]

    if(first_group_length!=0):
        groups.append(first_group_length)
    for i in range(first_group_length,n_length,3):
        groups.append(n_str[i:i+3])

    result= ",".join(groups)
    return result



n=int(input())
result=insert_comma(n)
print(result)

