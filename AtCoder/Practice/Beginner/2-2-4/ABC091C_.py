inf = float('inf')
N = int(input())
A = []
B = []
for _ in range(N):
    A.append(tuple(map(int, input().split())))
for _ in range(N):
    B.append(tuple(map(int, input().split())))
B.sort(key=lambda t: t[0])

count = 0
for i in range(N):
    x, y = B[i]
    max_y = -1
    idx = -1
    for j in range(len(A)):
        tx, ty = A[j]
        if x > tx and y > ty:
            if max_y < ty:
                max_y = ty
                idx = j
    if idx >= 0:
        A.pop(idx)
        count += 1
print(count)
