# Problem: https://www.hackerrank.com/challenges/py-set-difference-operation/problem

input()
eng_set = set(input().split())
input()
fre_set = set(input().split())
difference_set = eng_set.difference(fre_set)
print(len(difference_set))