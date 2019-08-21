# mod=10**9+7
# N, M = map(int, input().split())
# A = [int(input()) for m in range(M)]
# L = [1 for n in range(N+1)]
# for a in A:
#   L[a]=0
# Block=[0,1]
# for n in range(1,N+1):
#   if L[n]==1:
#     Block=Block[1:]+[sum(Block)%mod]
#   else:
#     Block=Block[1:]+[0]
# print(Block[-1])

N, M = map(int, input().split())
A = [int(input()) for m in range(M)]
A = set(A)
dp = [0]*(N+1)
dp[0] = 1
if 1 in A:
    dp[1] = 0
else:
    dp[1] = 1
for i in range(2, N+1):
    if i in A:
        dp[i] = 0
    else:
        dp[i] = dp[i-1]+dp[i-2]
print(dp[N] % 1000000007)
