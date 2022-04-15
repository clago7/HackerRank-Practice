# Problem: https://www.hackerrank.com/challenges/piling-up/problem

from collections import deque
for test in range(int(input())):
    num_cubes, d = int(input()), deque(list(map(int, input().split(' '))))
    # print(d)
    for block in range(num_cubes-1):
        if d[0] >= d[1]:
            # print(f'Remove left - {d.popleft()}...\n"d" is now {d}')
            d.popleft()
        elif d[-1] >= d[-2]:
            # print(f'Remove right - {d.pop()}...\n"d" is now {d}')
            d.pop()
        else: break
        # else: print('Both the leftmost and rightmost cubes are smaller than the largest block.')
    if len(d) == 1:
        print('Yes')
    else: print('No')
        
