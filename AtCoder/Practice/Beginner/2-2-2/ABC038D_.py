import bisect
INF = float('inf')

N = int(input())
boxes = []
for _ in range(N):
    w, h = map(int, input().split())
    boxes.append((w, h))
boxes = sorted(boxes, key=lambda x: (x[0], -x[1]))

DP = []
for w, h in boxes:
    i = bisect.bisect_left(DP, h)
    if i >= len(DP):
        DP.append(h)
    else:
        DP[i] = h
print(len(DP))
