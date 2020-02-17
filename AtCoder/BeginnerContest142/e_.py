import sys

INF = sys.maxsize
N, M = map(int, input().split())
costs = []
keys = []
for _ in range(M):
    a, b = map(int, input().split())
    cs = list(map(int, input().split()))
    costs.append(a)
    # 鍵を2進化で表す
    # e.g. N=5, cs={1,2,5} => key = 10011
    key = 0
    for c in cs:
        key |= 1<<(c-1)
    keys.append(key)

dp = [INF]*(2**N)
dp[0] = 0
for m in range(M):
    a = costs[m]
    key = keys[m]
    for i in range(2**N):
        # keyを追加した場合と追加しない場合のコストを比較
        dp[i|key] = min(dp[i|key], dp[i]+a)
ans = dp[-1]
if ans == INF:
    print(-1)
else:
    # dp[-1] = dp[2**N-1] = dp[0b11...11] = 全ての宝箱が開いたときの最小コスト
    print(dp[-1])


