N, M = map(int, input().split())
reqs = []
ans = 0
B = 0
for _ in range(M):
    a, b = map(int, input().split())
    reqs.append((a, b))
reqs = sorted(reqs, key=lambda x: x[1])
for i in range(M):
    a, b = reqs[i]
    if a >= B:
        B = b
        ans += 1
print(ans)
