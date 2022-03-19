# Problem: https://www.hackerrank.com/challenges/polar-coordinates/problem

import cmath
input_str = input()

if '+' in input_str:
    sign_pos = input_str.find('+')
    
else:
    if input_str[0] == '-':
        sign_pos = input_str[1:].find('-') + 1
        
    else: sign_pos = input_str.find('-')
j_pos = input_str.find('j')
x = int(input_str[:sign_pos])
y = int(input_str[sign_pos:j_pos])
print(abs(complex(x,y)))
print(cmath.phase(complex(x,y)))