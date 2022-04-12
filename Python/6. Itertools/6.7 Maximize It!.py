# Problem: https://www.hackerrank.com/challenges/maximize-it/problem

from itertools import product
KM = list(map(int, input().split(' ')))
K, M = KM[0], KM[1]
lists = []
for _ in range(K):
    new_list = list(map(int,input().split(' ')))
    N = new_list.pop(0)
    lists.append(new_list)
cart_prod = list(product(*lists))
# print(cart_prod)
Smax = 0
for tup in cart_prod:
    S = sum(i**2 for i in tup)%M
    if S > Smax:
        Smax = S
print(Smax)