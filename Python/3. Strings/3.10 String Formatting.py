# Problem: https://www.hackerrank.com/challenges/python-string-formatting/problem

def print_formatted(number):
    width = len(f'{number:b}')
    for i in range(1, number +1):
        print(f'{i:{width}d} {i:{width}o} {i:{width}X} {i:{width}b}')
        # (Decimal) (Octal) (Hexadecimal (Capitalised)) (Binary)

n = int(input('Input a single integer: '))
print_formatted(n)