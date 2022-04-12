# Problem: https://www.hackerrank.com/challenges/iterables-and-iterators/problem

from itertools import combinations

N = int(input())
inp = ''.join(input().split(' '))
K = int(input())
a_occ = 0
combi = list(combinations(inp, K))

for tup in combi:
    if tup.count('a') > 0:
        a_occ += 1
print(a_occ/len(combi))