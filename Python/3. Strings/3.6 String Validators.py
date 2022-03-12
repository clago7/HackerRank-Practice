# Problem: https://www.hackerrank.com/challenges/string-validators/problem

s = input("Please enter string: ")

tests = ['.isalnum()','.isalpha()','.isdigit()','.islower()','.isupper()']
for test in tests:
    result = False
    for char in s:            
        run_line = 'char' + test
        if eval(run_line):
            print(True)
            result = True
            break
    if result == False:
        print(False)

# alternatively...
# print(any([char.isalnum() for char in s]))
# print(any([char.isalpha() for char in s]))
# print(any([char.isdigit() for char in s]))
# print(any([char.islower() for char in s]))
# print(any([char.isupper() for char in s]))