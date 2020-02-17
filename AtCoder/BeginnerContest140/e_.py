N = int(input())
P = list(map(int, input().split()))

import itertools
a = list(itertools.combinations(range(0, N), 2))

dp = [[None for _ in range(N)] for _ in range(N)]

def dpcheck(i, j):
    if dp[i][j] is not None:
        return dp[i][j]
    target = P[i:j+1]
    target.sort()
    dp[i][j] = target
    return target

all = 0
for i in range(len(a)):
    target = dpcheck(a[i][0], a[i][1])
    all += target[-2]
print(all)
