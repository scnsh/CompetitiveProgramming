N, W = map(int, input().split())
wvs = []
for _ in range(N):
    wvs.append(list(map(int, input().split())))


def chmax(x, w1, w2, diff):
    if dp[x][w1] < dp[x-1][w2]+diff:
        dp[x][w1] = dp[x-1][w2]+diff
        return True
    return False


dp = [[0]*(W+1) for _ in range(N+1)]
for i in range(N):
    for sum_w in range(W+1):
        # 貰うDP
        if sum_w-wvs[i][0] >= 0:
            # 品物を選んだ場合(選ぶために必要な重さを減らした状態に価値を追加した状態と比較)
            chmax(i+1, sum_w, sum_w-wvs[i][0], wvs[i][1])
        chmax(i+1, sum_w, sum_w, 0)  # 品物を選んでない場合
print(max(dp[N]))
