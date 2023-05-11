import math

test_cases = int(input())

for i in range(test_cases):
    N, X, M = map(float, input().split())
    X = X / 100  # convert percentage to decimal
    years = math.ceil(math.log(M/N, 1+X))
    print(years)
