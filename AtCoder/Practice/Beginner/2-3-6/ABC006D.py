# https://qiita.com/python_walker/items/d1e2be789f6e7a0851e5
import bisect
N = int(input())
cards = []
for _ in range(N):
    cards.append(int(input()))
count = 0
LIS = [cards[0]]
for i in range(1, N):
    if cards[i] > LIS[-1]:
        LIS.append(cards[i])
    else:
        LIS[bisect.bisect_left(LIS, cards[i])] = cards[i]
        count += 1
print(count)

