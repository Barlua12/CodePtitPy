def count_prime_triplets(n):
    is_prime=[True]*(n+1)
    is_prime[0],is_prime[1]=False,False
    for i in range(2,int(n**0.5)+1):
        if is_prime[i]:
            for j in range(i*i,n+1,i):
                is_prime[j]=False

    count=0
    for p in range(2,n-6+1):
        if is_prime[p]and (is_prime[p+2] and is_prime[p+4] or is_prime[p+4]and is_prime[p+6]):
            count+=1
    return count
t=int(input())

while t>0:
    n=int(input())
    print(count_prime_triplets(n))
    n-=1