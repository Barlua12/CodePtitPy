t = int(input())

def slove(s):
    cnt=1
    l=len(s)
    for i in range(len(s)):
        if s[i]!=s[i-1]:
            print(cnt,end='')
            print(s[i-1],end='')
        else:
            cnt+=1
    print(cnt, end='')
    print(s[i - 1])

while t>0:
    s=input()
    slove(s)
    t-=1