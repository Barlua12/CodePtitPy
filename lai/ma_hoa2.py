p = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'

while True:
    t=input()
    if t[0]=='0':
        break
    k,s=t.split()
    k=int(k)
    res=""
    for i in s:
        res+= p[(p.find(i))%28]
    print(res[::-1])



