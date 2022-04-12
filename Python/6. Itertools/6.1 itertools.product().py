# Problem: https://www.hackerrank.com/challenges/itertools-product/problem

from itertools import product
A, B = list(map(int, input().split())), list(map(int, input().split()))
print(*list(product(A,B)), sep=' ') # optional to include sep=' '