# Problem: https://www.hackerrank.com/challenges/text-wrap/problem

import math
# import textwrap
# %%
def wrap(string, max_width):
    last_iter = int(math.ceil(len(string)/max_width))
    pos, result = 0, ''
    for _ in range(last_iter):
        if _ == last_iter - 1:
            result += string[pos:]
        else: result += string[pos:pos + max_width] + '\n'
        pos += max_width
    return result

    # alternatively
    # return textwrap.fill(string, max_width)
 # %%
string, max_width = input("Enter string: "), int(input("Enter max width: "))
result = wrap(string, max_width)
# %%
print(result)