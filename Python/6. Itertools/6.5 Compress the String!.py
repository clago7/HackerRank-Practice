# Problem: https://www.hackerrank.com/challenges/compress-the-string/problem

from itertools import groupby
inp, l = str(input()), []
# for key, group in groupby(inp):
#     l.append((len(list(group)),int(key)))
# print(*l)
print(*[(len(list(group)), int(key)) for key, group in groupby(inp)])