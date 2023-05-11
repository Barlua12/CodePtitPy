def count_triplets(arr, n):
    arr.sort()  # sắp xếp mảng
    count = 0
    for i in range(n - 2):
        left = i + 1
        right = n - 1
        while left < right:
            sum = arr[i] + arr[left] + arr[right]
            if sum == 0:
                count += 1
                left += 1
                right -= 1
            elif sum > 0:
                right -= 1
            else:
                left += 1
    return count

# Test
t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(count_triplets(arr, n))
