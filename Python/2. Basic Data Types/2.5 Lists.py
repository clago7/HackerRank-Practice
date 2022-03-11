# Problem: https://www.hackerrank.com/challenges/python-lists/problem

def lister(result):
    line = input().split()
    command = line[0]
    values = line[1:]
    if command == 'print':
        print(result)
    else:
        run_line = 'result.' + command + "(" + ",".join(values) + ")"
        eval(run_line)

result = []
for i in range(int(input())):
    lister(result)