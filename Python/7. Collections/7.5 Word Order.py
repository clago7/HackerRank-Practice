# Problem: https://www.hackerrank.com/challenges/word-order/problem

from collections import OrderedDict
words = OrderedDict()
for _ in range(int(input())):
    word = input()
    if word not in words:
        words[word] = 1
    else: words[word] += 1
print(len(words))
print(*words.values())