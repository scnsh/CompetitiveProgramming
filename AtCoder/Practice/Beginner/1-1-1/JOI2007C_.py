import bisect

N, M = map(int, input().split())
points = [0] + [int(input()) for _ in range(N)]
points.sort()
pairs = []
for a in range(N+1):
    for b in range(a, N+1):
        pairs.append(points[a]+points[b])
max_point = 0
pairs.sort()
for pair in pairs:
    index = max(bisect.bisect_left(pairs, M-pair)-1, 0)
    if M >= pair + pairs[index] >= max_point:
        max_point = pair+pairs[index]
print(max_point)
