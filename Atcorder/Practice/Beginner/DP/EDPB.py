import sys

inf = sys.maxsize
N, K = map(int, input().split())
heights = list(map(int, input().split()))

dp = [inf]*N
dp[0] = 0


def chmin(a, b, diff):
    if dp[a] > dp[b] + diff:
        dp[a] = dp[b] + diff
    return


for i in range(N):
    for j in range(1, K+1):
        if i-j >= 0:
            chmin(i, i-j, abs(heights[i]-heights[i-j]))

print(dp[N-1])
