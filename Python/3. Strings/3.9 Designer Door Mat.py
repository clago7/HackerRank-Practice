# Problem: https://www.hackerrank.com/challenges/designer-door-mat/problem

import math

input_list = [int(i) for i in input('Please input (breadth) and (length) of door mat (e.g. 11 33): ').split(' ')]
N, M = input_list[0], input_list[1]
mat, iterations = '.|.', math.floor(N/2)
# top half
for n in range(iterations):
    print((mat*(n*2+1)).center(M,'-'))

# middle welcome
print('WELCOME'.center(M,'-'))

# bottom half
for n in range(iterations):
    print((mat*((iterations-n)*2-1)).center(M,'-'))