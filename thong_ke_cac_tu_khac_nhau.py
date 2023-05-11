import re
from collections import Counter

n = int(input())
words = []
for i in range(n):
    line = input().lower()
    words.extend(re.findall(r'\b\w+\b', line))  # tách các từ trong dòng và thêm vào danh sách

word_count = Counter(words)  # đếm số lần xuất hiện của các từ
sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))  # sắp xếp theo thứ tự giảm dần số lần xuất hiện và tăng dần từ điển

for word, count in sorted_words:
    print(word, count)
