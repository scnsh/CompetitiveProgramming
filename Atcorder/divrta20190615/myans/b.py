import numpy as np
N = int(input())
pair_list = []
diff_list = {}
duplex = 0
for _ in range(N):
    new_pair = list(map(int, input().split()))
    if new_pair in pair_list:
        duplex += 1
    else:
        for pair in pair_list:
            diff = tuple(np.array(pair) - np.array(new_pair))
            if diff in diff_list:
                diff_list[diff] += 1
            else:
                diff_list[diff] = 1
        pair_list.append(new_pair)
if N == 1:
    print(N)
else:
    print(N - max(max(diff_list.values()), duplex))
