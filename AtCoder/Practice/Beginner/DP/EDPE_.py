import sys

inf = sys.maxsize
N, W = map(int, input().split())
wvs = []
v_len = 0
for _ in range(N):
    wvs.append(list(map(int, input().split())))
    v_len += wvs[-1][1]


def chmin(x, v1, v2, diff):
    if dp[x][v1] > dp[x-1][v2]+diff:
        dp[x][v1] = dp[x-1][v2]+diff
        return True
    return False


dp = [[inf]*(v_len+1) for _ in range(N+1)]
dp[0][0] = 0
for i in range(N):
    for sum_v in range(v_len+1):
        if sum_v-wvs[i][1] >= 0:
            # 品物を選んだ場合(選ぶために必要な価値を減らした状態に重さを追加した状態と比較)
            chmin(i+1, sum_v, sum_v-wvs[i][1], wvs[i][0])
        chmin(i+1, sum_v, sum_v, 0)  # 品物を選んでない場合
max_i = 0
for i in range(v_len+1):
    if dp[N][i] <= W and max_i < i:
        max_i = i
print(max_i)
