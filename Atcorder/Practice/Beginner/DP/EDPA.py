import sys

inf = sys.maxsize

N = int(input())
heights = list(map(int, input().split()))

# DPテーブルの初期化(最小問題なのでINFで初期化
dp = [inf] * N

# 初期条件
dp[0] = 0


def chmin(a, b, diff):
    if dp[a] > dp[b]+diff:
        dp[a] = dp[b]+diff
        return True
    return False


# 普通のDP
for i in range(1, N):
    chmin(i, i-1, abs(heights[i]-heights[i-1]))
    if i > 1:
        chmin(i, i-2, abs(heights[i]-heights[i-2]))
print(dp[N-1])


# # メモ化再帰
# def chmin(a, b):
#     if a > b:
#         a = b
#     return a
#
#
# def rec(i):
#     if dp[i] < inf:
#         return dp[i]
#     if i == 0:
#         return 0
#     res = inf
#     res = chmin(res, rec(i-1)+abs(heights[i]-heights[i-1]))
#     if i > 1:
#         res = chmin(res, rec(i-2)+abs(heights[i]-heights[i-2]))
#     dp[i] = res
#     return dp[i]
#
#
# print(rec(N-1))
