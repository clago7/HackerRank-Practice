# Problem: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

n = int(input())
arr = list(map(int, input().split()))

print(sorted(set(arr))[-2])
# alternatively
print(max([x for x in arr if x != max(arr)]))