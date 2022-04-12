# Problem: https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem

from itertools import combinations_with_replacement
inp = input().split(' ')
s, k = ''.join(sorted(inp[0])), int(inp[1])
for tup in list(combinations_with_replacement(s, k)):
    print(''.join(tup))