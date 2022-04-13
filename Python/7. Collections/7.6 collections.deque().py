# Problem: https://www.hackerrank.com/challenges/py-collections-deque/problem

from collections import deque
d = deque()
for _ in range(int(input())):
    eval_l = input().split(' ')
    if len(eval_l) > 1:
        mtd, val = eval_l[0], eval_l[1]
        # print(mtd, val)
        eval('d.'+mtd+'('+val+')')
    else:
        mtd = eval_l[0]
        eval('d.'+mtd+'()')
print(*d)