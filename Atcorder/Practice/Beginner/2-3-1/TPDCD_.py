N, D = map(int, input().split())

I = J = K = 0
while D % 2 == 0:
    I += 1
    D /= 2
while D % 3 == 0:
    J += 1
    D /= 3
while D % 5 == 0:
    K += 1
    D /= 5

if D == 1:

    dp = [[[[0] * (K + 1) for _ in range(J + 1)] for _ in range(I + 1)] for _ in range(N + 1)]
    dp[0][0][0][0] = 1

    for n in range(N):
        for i in range(I + 1):
            for j in range(J + 1):
                for k in range(K + 1):
                    per = dp[n][i][j][k] / 6
                    dp[n + 1][i][j][k] += per  # 1
                    dp[n + 1][min(i + 1, I)][j][k] += per  # 2
                    dp[n + 1][i][min(j + 1, J)][k] += per  # 3
                    dp[n + 1][min(i+2, I)][j][k] += per  # 4
                    dp[n + 1][i][j][min(k+1, K)] += per  # 5
                    dp[n + 1][min(i + 1, I)][min(j + 1, J)][k] += per  # 6
    print(dp[N][I][J][K])
else:
    print(0)
