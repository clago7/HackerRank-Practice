# Problem:https://www.hackerrank.com/challenges/py-set-mutations/problem

input()
set_A = set(map(int,input().split()))
for _ in range(int(input())):
    command = input().split()[0]
    new_set = set(map(int,input().split()))
    run_line = 'set_A.'+command+'(new_set)'
    eval(run_line)
print(sum(i for i in set_A))