# Problem: https://www.hackerrank.com/challenges/py-check-subset/problem

T = int(input())
for test in range(T):
    input()
    set_A = set(map(int, input().split()))
    input()
    set_B = set(map(int, input().split()))
    union_set = set_A.union(set_B)
    if union_set == len:
        print(True)
    else: print(False)