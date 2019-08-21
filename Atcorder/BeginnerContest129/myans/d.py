from itertools import product
import numpy as np

H, W = map(int, input().split())
grid = []
for _ in range(H):
    array = list(input())
    grid.append(array)
b = np.array(grid)
b = np.where(b == ".", 1, 0)

L = np.zeros((H, W), dtype=np.int)
R = np.zeros((H, W), dtype=np.int)
D = np.zeros((H, W), dtype=np.int)
U = np.zeros((H, W), dtype=np.int)

for i in range(1, H):
    L[i] += (L[i-1]+1)*b[i-1]

for i in range(H-2, -1, -1):
    R[i] += (R[i+1]+1)*b[i+1]

for i in range(1, W):
    U[:, i] += (U[:, i-1]+1)*b[:, i-1]

for i in range(W-2, -1, -1):
    D[:, i] += (D[:, i+1]+1)*b[:, i+1]

answer = ((L+R+U+D)*b).max()

print(answer+1)
