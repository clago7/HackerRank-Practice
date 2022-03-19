# Problem: https://www.hackerrank.com/challenges/py-check-strict-superset/problem

set_A = set(input().split())
n = int(input())
ind = 0
for _ in range(n):
    set_n = set(input().split())
    union_set = set_A.union(set_n)
    if (union_set == set_A) and (len(set_A) > len(set_n)):
        ind += 1
if ind == n:
    print(True)
else: print(False)