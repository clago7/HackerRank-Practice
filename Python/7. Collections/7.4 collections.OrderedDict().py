# Problem: https://www.hackerrank.com/challenges/py-collections-ordereddict/problem

from collections import OrderedDict
ordered_dict = OrderedDict()
for item in range(int(input())):
    item_name, price = [], 0
    inps = input().split(' ')
    for inp in inps:
        if inp.isalpha():
            item_name.append(inp)
        else: price = int(inp)
    item_name = ' '.join(item_name)
    if item_name not in ordered_dict:
        ordered_dict[item_name] = price
    else: ordered_dict[item_name] += price
for item_name, net_price in ordered_dict.items():
    print(f'{item_name} {str(net_price)}')