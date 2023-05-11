t=input()

count_thuong=0
count_hoa=0
for i in range(len(t)):
    if(t[i].isupper()):
        count_hoa+=1
    if(t[i].islower()):
        count_thuong+=1
if(count_thuong>=count_hoa):
    print(t.lower())
else:print(t.upper())