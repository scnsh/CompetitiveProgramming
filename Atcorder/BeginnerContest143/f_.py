from collections import Counter

N = int(input())
A = list(map(int, input().split()))

C = [0] * (N + 1)
S = [0] * (N + 1)

for a in Counter(A).values():
    C[a] += 1
    S[a] += a

for i in range(1, N + 1):
    C[i] += C[i - 1]
    S[i] += S[i - 1]

for K in range(1, N + 1):
    ok, ng = 0, N + 1
    while ng - ok > 1:
        mid = (ng + ok) // 2
        if S[mid] + mid * (C[-1] - C[mid]) >= K * mid:
            ok = mid
        else:
            ng = mid
    print(ok)
