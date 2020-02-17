import numpy as np

W = int(input())
N, K = map(int, input().split())
A = []
B = []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

dp = np.zeros((K+1, W+1)).astype('i')

for i in range(N):
    if W >= A[i]:
        dp[1:, A[i]:] = np.maximum(dp[:K, :W+1-A[i]]+B[i], dp[1:, A[i]:])

print(dp[K, W])
