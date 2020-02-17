N = int(input())

ABC = []
for _ in range(N):
    ABC.append(list(map(int, input().split())))


def chmax(i, j):
    diff = max([dp[i-1][x] for x in {0, 1, 2}-{j}])
    if dp[i][j] < ABC[i][j] + diff:
        dp[i][j] = ABC[i][j] + diff
        return True
    return False


dp = [[0, 0, 0] for _ in range(N)]
dp[0][0] = ABC[0][0]
dp[0][1] = ABC[0][1]
dp[0][2] = ABC[0][2]


for i in range(N-1):
    for j in range(3):
        chmax(i+1, j)
    # dp[i+1][0] = ABC[i+1][0] + max(dp[i][1], dp[i][2])
    # dp[i+1][1] = ABC[i+1][1] + max(dp[i][0], dp[i][2])
    # dp[i+1][2] = ABC[i+1][2] + max(dp[i][0], dp[i][1])
print(max(dp[N-1][0], dp[N-1][1], dp[N-1][2]))
