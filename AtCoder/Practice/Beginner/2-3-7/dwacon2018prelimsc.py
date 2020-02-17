n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))


def solve(a, b):
    c = [1]
    for i, j in zip(a, a[1:]):
        c += [c[-1]*(i==j)+1]
    dp = [0]*(sum(b)+1)
    dp[0] = 1
    for i in c:
        for j in range(i, len(dp)):
            dp[j] += dp[j-i]
    return dp[-1]


print(solve(a, b)*solve(b, a) % (10**9+7))
