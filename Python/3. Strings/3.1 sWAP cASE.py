# Problem: https://www.hackerrank.com/challenges/swap-case/problem

def swap_case(s):
    result = ''
    for elem in s:
        if elem.isupper():
            elem = elem.lower()
        elif elem.islower():
            elem = elem.upper()
        result += elem
    return result

s = input()
result = swap_case(s)
print(result)