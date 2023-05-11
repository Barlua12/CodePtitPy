P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while True:
    K, S = input().split()
    K = int(K)
    if K == 0:
        print('')
        break
    encoded = ""
    for i in range(len(S)):
        encoded += P[(P.index(S[i]) + K) % 28]
    reversed_str = ""
    for i in range(len(encoded)):
        reversed_str = encoded[i] + reversed_str
    print(reversed_str)
