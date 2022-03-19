# Problem: https://www.hackerrank.com/challenges/symmetric-difference/problem

M, a = int(input()),set(map(int,input().split()))
N, b = int(input()),set(map(int,input().split()))
diff = a.difference(b)
diff.update(b.difference(a))
sorted_diff = sorted(list(diff))
[print(i) for i in sorted_diff]