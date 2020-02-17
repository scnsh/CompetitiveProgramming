import numpy as np
L, R = list(map(int, input().split()))

min_val = 2019
for i in range(L, R):
    for j in range(i+1, R+1):
        val = (i*j) % 2019
        if min_val > val:
            min_val = val
            if min_val == 0:
                break
    if min_val == 0:
        break
print(min_val)
