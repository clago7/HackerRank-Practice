# Problem: https://www.hackerrank.com/challenges/py-set-difference-operation/problem

input()
eng_set = set(input().split())
input()
fre_set = set(input().split())
sym_difference_set = eng_set.symmetric_difference(fre_set)
print(len(sym_difference_set))