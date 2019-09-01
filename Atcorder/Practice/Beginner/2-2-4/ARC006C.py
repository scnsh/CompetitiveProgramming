inf = float('inf')
N = int(input())
boxes = [list() for _ in range(N)]
boxes[0].append(int(input()))
num = 1
for _ in range(N-1):
    box = int(input())
    min_diff = inf
    idx = -1
    for i in range(num):
        diff = boxes[i][-1] - box
        if min_diff > diff >= 0:
            idx = i
            min_diff = diff
    if idx >= 0:
        boxes[idx].append(box)
    else:
        boxes[num].append(box)
        num += 1
print(num)
