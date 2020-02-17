import bisect

N = int(input())
L = sorted(([int(x) for x in input().split()]))

count = 0
for i in range(N - 1, -1, -1):
    for j in range(i - 1, -1, -1):
        # L[j] は L[i]以下の集合を降順で参照する
        k = bisect.bisect_left(L, L[i] + L[j])
        # L[i]+L[j] > k > L[j]
        count += k - (i + 1)
print(count)
