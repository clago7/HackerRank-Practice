# Problem: https://www.hackerrank.com/challenges/py-set-union/problem

input()
eng_set = set(input().split())
input()
fre_set = set(input().split())
union_set = eng_set.union(fre_set)
print(len(union_set))