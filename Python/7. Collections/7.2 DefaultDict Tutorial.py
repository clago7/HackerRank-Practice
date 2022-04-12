# Problem: https://www.hackerrank.com/challenges/defaultdict-tutorial/problem

nm = list(map(int, input().split()))
n, m = nm[0], nm[1]
grpA, grpB = [], []
[grpA.append(input()) for _ in range(n)]
[grpB.append(input()) for _ in range(m)]
for Bword in grpB:
    inds = []
    if grpA.count(Bword) == 0:
        inds.append(-1)
    else:
        [inds.append(ind+1) for ind, Aword in enumerate(grpA) if Bword == Aword]
    print(*inds, sep=' ')