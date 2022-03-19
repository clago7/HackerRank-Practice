# Problem: https://www.hackerrank.com/challenges/py-the-captains-room/problem

k, rm_nums = int(input()), input().split()
grps = set(rm_nums)
for grp in grps:
    count = 0
    for num in rm_nums:
        if num == grp:
            count += 1
        if count > 1:
            break
    if count == 1:
        print(grp)
        break