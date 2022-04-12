# Problem: https://www.hackerrank.com/challenges/itertools-combinations/problem

from itertools import combinations
inp = input().split(' ')
s, k = ''.join(sorted(inp[0])), int(inp[1])
for i in range(1, k+1):
    for tup in list(combinations(s, i)):
        print(''.join(tup))