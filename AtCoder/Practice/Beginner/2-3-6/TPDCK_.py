# https://suikaba.hatenablog.com/entry/2017/08/24/001235
import bisect

N = int(input())
LR = []
for _ in range(N):
    x, r = map(int, input().split())
    LR.append((x+r, x-r))
LR.sort(reverse=True)

LIS = []
for r, l in LR:
    i = bisect.bisect_left(LIS, l)
    if i == len(LIS):
        LIS.append(l)
    else:
        LIS[i] = l

print(len(LIS))
