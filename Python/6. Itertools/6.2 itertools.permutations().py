# Problem: https://www.hackerrank.com/challenges/itertools-permutations/problem

from itertools import permutations
input_l = str(input()).split(" ")
s, k = ''.join(sorted(input_l[0])), int(input_l[1])
for tup in list(permutations(s, k)):
    print(''.join(tup))