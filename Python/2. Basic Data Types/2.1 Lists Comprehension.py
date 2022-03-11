# Problem: https://www.hackerrank.com/challenges/list-comprehensions/problem

x, y , z, n = int(input()), int(input()), int(input()), int(input()), int(input())
permutations = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k!=n]
print(permutations)