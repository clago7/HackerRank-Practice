# Problem: https://www.hackerrank.com/challenges/most-commons/problem

from collections import Counter
s = input()
top_letters = Counter(sorted(list(s))).most_common(3)
[print(*record) for record in top_letters]