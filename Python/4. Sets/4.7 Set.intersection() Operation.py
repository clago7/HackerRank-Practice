# Problem: https://www.hackerrank.com/challenges/py-set-intersection-operation/problem

input()
eng_set = set(input().split())
input()
fre_set = set(input().split())
intersect_set = eng_set.intersection(fre_set)
print(len(intersect_set))
