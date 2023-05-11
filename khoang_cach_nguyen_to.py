def prime_numbers(n):
    primes = []
    candidate = 2
    while len(primes) < n:
        is_prime = True
        for prime in primes:
            if candidate % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(candidate)
        candidate += 1
    return primes
def consecutive_numbers(n, x):
    primes = prime_numbers(n)
    result = [x]
    for i in range(n):
        result.append(result[-1] + primes[i])
    return result
n, x = map(int, input().split())
for number in consecutive_numbers(n, x):
    print(number, end=' ')
print()
