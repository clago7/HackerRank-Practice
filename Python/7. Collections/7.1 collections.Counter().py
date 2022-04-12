# Problem: https://www.hackerrank.com/challenges/collections-counter/problem

from collections import Counter
input()
myList = list(map(int, input().split(' ')))
stock = Counter(myList)
earnings = 0
for cust in range(int(input())):
    order = list(map(int, input().split(' ')))
    size, dollar = order[0], order[1]
    if stock[size] > 0:
        earnings += dollar
        stock[size] = max(0, stock[size]-1)
    else: continue
print(earnings)