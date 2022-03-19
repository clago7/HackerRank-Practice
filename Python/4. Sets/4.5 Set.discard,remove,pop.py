# Problem: https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem

n = int(input())
s = set(map(int, input().split()))
for _ in range(int(input())):
    command = str(input()).split()
    if len(command) < 2:
        run_line = 's.' + str(command[0]) + '()'
    else: run_line = 's.' + str(command[0]) + '(' + str(command[1]) + ')'
    eval(run_line)
print(sum(i for i in s))