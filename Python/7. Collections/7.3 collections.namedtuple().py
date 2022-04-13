# Problem: https://www.hackerrank.com/challenges/py-collections-namedtuple/problem

from collections import namedtuple
n, Records = int(input()), namedtuple('Records', input())
print(f'{sum([int(Records(*input().split()).MARKS) for stud in range(n)])/n:.2f}')