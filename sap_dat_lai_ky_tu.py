T = int(input())  # số bộ test

for t in range(1, T+1):
    s1 = input().strip()  # xâu s1
    s2 = input().strip()  # xâu s2
    if len(s1) != len(s2):
        print(f"Test {t}: NO")  # nếu độ dài khác nhau thì s2 không phải là sắp đặt lại của s1
    else:
        count1 = [0] * 26  # mảng đếm cho s1, khởi tạo toàn bộ phần tử bằng 0
        count2 = [0] * 26  # mảng đếm cho s2, khởi tạo toàn bộ phần tử bằng 0
        for c in s1:
            count1[ord(c) - ord('a')] += 1  # tăng giá trị tương ứng trong mảng đếm của s1
        for c in s2:
            count2[ord(c) - ord('a')] += 1  # tăng giá trị tương ứng trong mảng đếm của s2
        if count1 == count2:  # so sánh hai mảng đếm
            print(f"Test {t}: YES")
        else:
            print(f"Test {t}: NO")
