# Problem: https://www.hackerrank.com/challenges/python-mutations/problem

def mutate_string(string, position, character):
    return string[:position] + character + string[position+1:]

#alternatively...
# def mutate_string(string, position, character):
#     l = list(string)
#     l[position] = character
#     return ''.join(l)

s = input()
i, c = input().split()
s_new = mutate_string(s, int(i), c)
print(s_new)